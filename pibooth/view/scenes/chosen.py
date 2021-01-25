from pgi import require_version

from pibooth.view.scenes.paths import common_media_path, choose_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER, PoolingTimer


class ChosenScene(Scene):
    app = None

    def __init__(self, app, choices):
        super(ChosenScene, self).__init__()
        LOGGER.info("new ChosenScene")

        self.timer = PoolingTimer(4)

        self.app = app
        self._setup(choices)

    def _setup(self, choice):
        self.set_background(common_media_path('BG-Blank.png'),
                            common_media_path('BG-Blank.png'))

        LOGGER.info(choice)

        # Summary of choice
        self.add_widget(
            Gtk.Image.new_from_file(choose_media_path('choice_po_' + str(choice) + '.png')),
            Placement(0.5, 0.65, 1),
            Placement(0.5, 0.65, 1)
        )

    def startTimer(self):
        self.timer.start()
        while True:
            if self.timer.is_timeout():
                LOGGER.info("timeout")
                break
        self._startPreview()

    def _startPreview(self):
        self.app.goToPreviewStep()
