from pgi import require_version

from pibooth.view.scenes.paths import processing_media_path

require_version('Gtk', '3.0')

from pibooth.view.scene import Scene
from pibooth.utils import LOGGER


class ProcessingScene(Scene):
    app = None

    def __init__(self, app):
        super(ProcessingScene, self).__init__()
        LOGGER.info("new ProcessingScene")

        self.app = app
        self._setup()

    def _setup(self):
        self.set_background(processing_media_path('BG-Chosen.png'),
                            processing_media_path('BG-Chosen.png'))
