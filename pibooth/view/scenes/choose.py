from pgi import require_version

from pibooth.view.scenes.paths import common_media_path

require_version('Gtk', '3.0')

from pibooth.view.scene import Scene
from pibooth.utils import LOGGER


class ChooseScene(Scene):
    app = None

    def __init__(self, app, choices):
        super(ChooseScene, self).__init__()
        LOGGER.info("new ChooseScene")
        self.app = app
        self._setup(choices)

    def _setup(self, choices):
        self.set_background(common_media_path('BG-Blank.png'),
                            common_media_path('BG-Blank.png'))

        # Add choices
        if choices & len(choices) == 2:
            LOGGER.info(choices[0])
            LOGGER.info(choices[1])
