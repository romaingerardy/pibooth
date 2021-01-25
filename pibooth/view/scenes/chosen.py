import threading

from pgi import require_version

from pibooth.view.scenes.paths import common_media_path, choose_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER, PoolingTimer

#import threading

class ChosenScene(Scene):
    app = None

    def __init__(self, app, choices):
        super(ChosenScene, self).__init__()
        LOGGER.info("new ChosenScene")

        self.timer = PoolingTimer(10)

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
        #time.sleep(4)
        t = threading.Timer(4, self._startPreview)
        t.start()
        #threading.Timer(5, lambda: self._startPreview).start()
        #self.timer.start()
        #while True:
        #    if self.timer.is_timeout():
        #        LOGGER.info("timeout")
        #        break
        self._startPreview()

    def _startPreview(self):
        self.app.goToPreviewStep()
