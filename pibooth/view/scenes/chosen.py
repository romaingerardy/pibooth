import threading

from pgi import require_version

from pibooth.view.scenes.paths import choose_media_path, chosen_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER

import faulthandler

faulthandler.enable()

class ChosenScene(Scene):
    app = None

    TIMEOUT = 3

    def __init__(self, app, choices):
        super(ChosenScene, self).__init__()
        LOGGER.info("new ChosenScene")

        # self.timer = PoolingTimer(10)

        self.app = app
        self._setup(choices)

    def _setup(self, choice):
        self.set_background(chosen_media_path('BG-Chosen.png'),
                            chosen_media_path('BG-Chosen.png'))

        LOGGER.info(choice)

        # Summary of choice
        self.add_widget(
            Gtk.Image.new_from_file(choose_media_path('choice_po_' + str(choice) + '.png')),
            Placement(0.5, 0.65, 1),
            Placement(0.5, 0.65, 1)
        )

    def startTimer(self):
        t = threading.Timer(self.TIMEOUT, self._startPreview)
        t.start()
        LOGGER.info("timer started")

    def _startPreview(self):
        LOGGER.info("goToPreviewStep")
        self.app.goToPreviewStep()
