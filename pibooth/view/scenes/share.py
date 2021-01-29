from pgi import require_version

from pibooth.view.scenes.paths import share_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk
from pibooth.common.buttons import OrangeButton, PixButton

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER


class ShareScene(Scene):

    def __init__(self, app, previous_picture_file):
        super(ShareScene, self).__init__()
        LOGGER.info("new ShareScene")
        self.app = app
        self.previous_picture = previous_picture_file
        self._setup()

    def _setup(self):
        self.set_background(share_media_path('BG-Share.png'),
                            share_media_path('BG-Share.png'))

        # Show final picture
        LOGGER.info("show final picture")
        self.add_widget(
            Gtk.Image.new_from_file(self.previous_picture),
            Placement(0.1, 0.71, 0.23),
            Placement(0.1, 0.71, 0.23)
        )
        LOGGER.info("after show final picture")

        # Add share buttons
        # print_button = Gtk.Button.new_with_label("Imprimer")
        # print_button.connect("clicked", self.on_click_me_clicked)
        # quit_button = Gtk.Button.new_with_label("Terminer")
        # quit_button.connect("clicked", self.on_click_quit)

        print_button = PixButton('Imprimer')
        quit_button = PixButton('Terminer')
        self.add_widget(
            print_button,
            Placement(0.7, 0.7, 1),
            Placement(0.7, 0.7, 1),
            self._on_click_quit
        )
        self.add_widget(
            quit_button,
            Placement(0.7, 0.8, 1),
            Placement(0.7, 0.8, 1),
            self._on_click_quit
        )

    def _on_click_quit(self):
        # Go to wait screen
        self.app.goToWaitStep()
