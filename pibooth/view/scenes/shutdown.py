import time

from pgi import require_version

from pibooth.common.buttons import RectButton
from pibooth.view.scenes.paths import common_media_path, wait_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER


class ShutdownScene(Scene):

    def __init__(self, window):
        super(ShutdownScene, self).__init__()
        self.clickable = False
        self.window = window
        self._setup()
        self.clickable = True
        time.sleep(1)

    def _setup(self):
        self.set_background(common_media_path('BG-Blank.png'),
                            common_media_path('BG-Blank.png'))

        # Add icon
        self.add_widget(
            Gtk.Image.new_from_file(wait_media_path('shutdown_icon.png')),
            Placement(0.5, 0.1, 1),
            Placement(0.5, 0.1, 1)
        )

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
        if self.clickable:
            LOGGER.info("!!! Shutdown asked !")
            self.window.hide_shutdown()

    def _on_cancel(self, widget):
        if self.clickable:
            LOGGER.info("!!! Cancel shutdown")
            self.window.hide_shutdown()
