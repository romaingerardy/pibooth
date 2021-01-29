import threading

from pgi import require_version

from pibooth.utils import LOGGER
from pibooth.view.scenes.paths import finish_media_path

require_version('Gtk', '3.0')

from pibooth.view.scene import Scene


class FinishScene(Scene):
    TIMEOUT = 2

    def __init__(self, app):
        super(FinishScene, self).__init__()
        self.app = app
        self._setup()

    def _setup(self):
        self.set_background(finish_media_path('BG-ThankYou.png'),
                            finish_media_path('BG-ThankYou.png'))

    def startTimer(self):
        t = threading.Timer(self.TIMEOUT, self._callable)
        t.start()
        LOGGER.info("timer started")

    def _callable(self):
        LOGGER.info("goToWaitStep")
        self.app.goToWaitStep()
