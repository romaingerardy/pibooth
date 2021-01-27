from pgi import require_version

from pibooth.common.buttons import RectButton
from pibooth.view.scenes.paths import common_media_path

require_version('Gtk', '3.0')

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER


class ShutdownScene(Scene):
    app = None

    def __init__(self, window):
        super(ShutdownScene, self).__init__()
        self.window = window
        self._setup()

    def _setup(self):
        self.set_background(common_media_path('BG-Blank.png'),
                            common_media_path('BG-Blank.png'))

        # Add Menu buttons
        cancel_button = RectButton('Annuler', False)
        cancel_button.connect("clicked", self._on_cancel)
        self.add_widget(
            cancel_button,
            Placement(0.4, 0.5, 1),
            Placement(0.4, 0.5, 1)
        )

        quit_button = RectButton('Eteindre', True)
        quit_button.connect("clicked", self._on_quit)
        self.add_widget(
            quit_button,
            Placement(0.6, 0.5, 1),
            Placement(0.6, 0.5, 1)
        )

    def _on_quit(self, widget):
        # Go to wait screen
        LOGGER.info("!!! Shutdown asked !")
        self.window.hide_shutdown()

    def _on_cancel(self, widget):
        # Go to wait screen
        LOGGER.info("!!! Cancel shutdown")
        self.window.hide_shutdown()
