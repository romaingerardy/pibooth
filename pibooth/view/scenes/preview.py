from pgi import require_version

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
