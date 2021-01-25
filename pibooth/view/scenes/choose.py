from pgi import require_version

from pibooth.view.scenes.paths import choose_media_path

require_version('Gtk', '3.0')

from pibooth.view.scene import Scene
from pibooth.utils import LOGGER


class ChooseScene(Scene):
    app = None

    def __init__(self, app):
        super(ChooseScene, self).__init__()
        LOGGER.info("new ChooseScene")
        self.app = app
        self._setup()

    def _setup(self):
        self.set_background(choose_media_path('BG-Layout.png'),
                            choose_media_path('BG-Layout.png'))
