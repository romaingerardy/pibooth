# -*- coding: utf-8 -*-

import os
import os.path as osp
from io import BytesIO

import pibooth
from pibooth.utils import LOGGER, timeit


class GifPlugin(object):
    size = (500, 500)  # GIF size (square)
    num_frame = 8  # Number of frames in Gif
    gif_delay = 15  # Frame delay [ms]
    rebound = True  # Create a video that loops start <=> end

    """Plugin to manage the gif captures.
    """

    def __init__(self, plugin_manager):
        self._pm = plugin_manager
        self.count = 0

    @pibooth.hookimpl
    def state_preview_exit(self, cfg, app):
        if cfg.getboolean('WINDOW', 'preview_stop_on_capture'):
            app.camera.stop_preview()

    @pibooth.hookimpl
    def state_capture_do(self, cfg, app, win):

        if app.capture_nbr != 8:
            # Only available for GIF
            return

        app.camera.capture_gif(self.size, self.num_frame, self.gif_delay, self.rebound)

    @pibooth.hookimpl
    def state_processing_do(self, cfg, app):

        if app.capture_nbr != 8:
            # Only available for GIF
            return

        LOGGER.info("state_processing_do")

        with timeit("Saving raw captures"):
            captures = app.camera.get_captures()

            for savedir in cfg.gettuple('GENERAL', 'directory', 'path'):
                rawdir = osp.join(savedir, "raw", app.capture_date)
                os.makedirs(rawdir)

            # Save the frames as animated GIF to BytesIO
            animated_gif = BytesIO()
            captures[0].save(animated_gif,
                             format='GIF',
                             save_all=True,
                             append_images=captures[1:],  # Pillow >= 3.4.0
                             delay=0.1,
                             loop=4)
            animated_gif.seek(0, 2)
            LOGGER.info('GIF image size = ', animated_gif.tell())
            app.previous_picture = None  # TODO ?

        with timeit("Creating the final animation on disk"):
            for savedir in cfg.gettuple('GENERAL', 'directory', 'path'):
                app.previous_picture_file = osp.join(savedir, app.gif_filename)
                # Write contents to file
                animated_gif.seek(0)
                open(app.previous_picture_file, 'wb').write(animated_gif.read())
