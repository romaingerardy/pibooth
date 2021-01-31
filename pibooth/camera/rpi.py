# -*- coding: utf-8 -*-

import subprocess
import time
from io import BytesIO

from PIL import Image

try:
    import picamera
except ImportError:
    picamera = None  # picamera is optional
from pibooth.utils import memorize, LOGGER
from pibooth.language import get_translated_text
from pibooth.camera.base import BaseCamera


@memorize
def rpi_camera_connected():
    """Return True if a RPi camera is found.
    """
    if not picamera:
        return False  # picamera is not installed
    try:
        process = subprocess.Popen(['vcgencmd', 'get_camera'],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _stderr = process.communicate()
        if stdout and u'detected=1' in stdout.decode('utf-8'):
            return True
    except OSError:
        pass
    return False


class RpiCamera(BaseCamera):
    """Camera management
    """

    if picamera:
        IMAGE_EFFECTS = list(picamera.PiCamera.IMAGE_EFFECTS.keys())
    else:
        IMAGE_EFFECTS = []

    def __init__(self,
                 iso=200,
                 resolution=(1920, 1080),
                 rotation=0,
                 flip=False,
                 delete_internal_memory=False):
        BaseCamera.__init__(self, resolution, delete_internal_memory)
        self._cam = picamera.PiCamera()
        self._cam.framerate = 15  # Slower is necessary for high-resolution
        self._cam.video_stabilization = True
        self._cam.vflip = False
        self._cam.hflip = flip
        self._cam.resolution = resolution
        self._cam.iso = iso
        self._cam.rotation = rotation

    def _show_overlay(self, text, alpha):
        """Add an image as an overlay.
        """
        if self._window:  # No window means no preview displayed

            img = self._window.preview_scene.get_countdown_overlay(text)
            if img:
                pad = Image.new('RGBA', (
                    ((img.size[0] + 31) // 32) * 32,
                    ((img.size[1] + 15) // 16) * 16,
                ))
                pad.paste(img, (0, 0), img)
                self._overlay = self._cam.add_overlay(pad.tobytes(), size=img.size)
                self._overlay.alpha = 255
                self._overlay.layer = 3

    def _hide_overlay(self):
        """Remove any existing overlay.
        """
        LOGGER.info("_hide_overlay")
        if self._overlay:
            LOGGER.info("Hide camera overlay")
            self._cam.remove_overlay(self._overlay)
            self._overlay = None

    def _post_process_capture(self, capture_data):
        """Rework capture data.

        :param capture_data: binary data as stream
        :type capture_data: :py:class:`io.BytesIO`
        """
        # "Rewind" the stream to the beginning so we can read its content
        capture_data.seek(0)
        return Image.open(capture_data)

    def preview(self, window, flip=True):
        """Display a preview on the given Rect (flip if necessary).
        """
        if self._cam.preview is not None:
            # Already running
            return

        self._window = window
        # rect = self.get_rect()
        if self._cam.hflip:
            if flip:
                # Don't flip again, already done at init
                flip = False
            else:
                # Flip again because flipped once at init
                flip = True

        self._cam.start_preview()
        # self._cam.start_preview(resolution=(rect.width, rect.height), hflip=flip,
        #                        fullscreen=False, window=tuple(rect))

    def preview_countdown(self, timeout, alpha=60):
        """Show a countdown of `timeout` seconds on the preview.
        Returns when the countdown is finished.
        """
        timeout = int(timeout)
        if timeout < 1:
            raise ValueError("Start time shall be greater than 0")
        if not self._cam.preview:
            raise EnvironmentError("Preview shall be started first")

        while timeout > 0:
            self._show_overlay(timeout, alpha)
            time.sleep(1)
            timeout -= 1
            print("Timeout " + str(timeout))
            self._hide_overlay()

        self._show_overlay(get_translated_text('smile'), alpha)

    def preview_wait(self, timeout, alpha=60):
        """Wait the given time.
        """
        time.sleep(timeout)
        self._show_overlay(get_translated_text('smile'), alpha)

    def stop_preview(self):
        """Stop the preview.
        """
        self._hide_overlay()
        self._cam.stop_preview()
        self._window = None

    def capture(self, effect=None):
        """Capture a new picture in a file.
        """
        effect = str(effect).lower()
        if effect not in self.IMAGE_EFFECTS:
            raise ValueError("Invalid capture effect '{}' (choose among {})".format(effect, self.IMAGE_EFFECTS))

        try:
            stream = BytesIO()
            self._cam.image_effect = effect
            self._cam.capture(stream, format='jpeg')
            self._captures.append(stream)
        finally:
            self._cam.image_effect = 'none'

        self._hide_overlay()  # If stop_preview() has not been called

    def capture_gif(self, size=(500, 500), num_frame=8, gif_delay=15, boomerang=True):

        LOGGER.info("Capturing GIF...")

        for i in range(num_frame):
            frame = Image.new("RGB", size, (25, 25, 255 * (num_frame - i) // num_frame))
            # Saving/opening is needed for better compression and quality
            fobj = BytesIO()
            frame.save(fobj, 'GIF')
            frame = Image.open(fobj)
            self._captures.append(frame)

        self._hide_overlay()

    def quit(self):
        """Close the camera driver, it's definitive.
        """
        self._cam.close()
