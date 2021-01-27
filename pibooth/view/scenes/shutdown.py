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
        LOGGER.info("new ShutdownScene")
        self.window = window
        self._setup()

    def _setup(self):
        self.set_background(common_media_path('BG-Blank.png'),
                            common_media_path('BG-Blank.png'))

        # Add Menu buttons
        quit_button = RectButton('Eteindre', True)
        self.add_widget(
            quit_button,
            Placement(0.5, 0.5, 1),
            Placement(0.5, 0.5, 1),
            self._on_click_quit
        )
        cancel_button = RectButton('Annuler', False)
        self.add_widget(
            cancel_button,
            Placement(0.7, 0.5, 1),
            Placement(0.7, 0.5, 1),
            self._on_click_quit
        )

    def _on_click_quit(self):
        # Go to wait screen
        LOGGER.info("Shutdown asked !")
        self.window.hide_shutdown(self)

    def _on_cancel_quit(self):
        # Go to wait screen
        self.window.hide_shutdown(self)
