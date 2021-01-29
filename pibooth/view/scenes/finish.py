from pgi import require_version

from pibooth.view.scenes.paths import finish_media_path

require_version('Gtk', '3.0')

from pibooth.view.scene import Scene


class FinishScene(Scene):

    def __init__(self, window):
        super(FinishScene, self).__init__()
        self.window = window
        self._setup()

    def _setup(self):
        self.set_background(finish_media_path('BG-ThankYou.png'),
                            finish_media_path('BG-ThankYou.png'))
