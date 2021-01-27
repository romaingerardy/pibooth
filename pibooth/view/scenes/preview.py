from PIL import Image
from pgi import require_version

from pibooth.view.scenes.paths import preview_media_path

require_version('Gtk', '3.0')

from pibooth.view.scene import Scene
from pibooth.utils import LOGGER


class PreviewScene(Scene):
    app = None

    def __init__(self, app):
        super(PreviewScene, self).__init__()
        LOGGER.info("new PreviewScene")

        self.app = app
        self._setup()

    def _setup(self):
        self.set_background(preview_media_path('BG-Preview.png'),
                            preview_media_path('BG-Preview.png'))

    def get_countdown_overlay(self, text):
        if str(text) == '3':
            img = Image.open(preview_media_path('countdown_3.png'))
        elif str(text) == '2':
            img = Image.open(preview_media_path('countdown_2.png'))
        elif str(text) == '1':
            img = Image.open(preview_media_path('countdown_1.png'))
        elif str(text) == '0':
            img = Image.open(preview_media_path('countdown_0.png'))
        else:
            LOGGER.warn("No countdown overlay for value '" + str(text) + "'")
            img = None

        return img
