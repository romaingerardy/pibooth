from pgi import require_version

#from pibooth.common.buttons import OrangeButton
from pibooth.view.scenes.paths import share_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk

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
        self.add_widget(
            Gtk.Image.new_from_file(self.previous_picture),
            Placement(0.1, 0.71, 0.23),
            Placement(0.1, 0.71, 0.23)
        )

        # Add share buttons
        #print_button = OrangeButton('Imprimer')
        #quit_button = OrangeButton('Terminer')

        #self.add_widget(
        #    print_button,
        #    Placement(0.7, 0.7, 1),
        #    Placement(0.7, 0.7, 1)
        #)
        #self.add_widget(
        #    quit_button,
        #    Placement(0.7, 0.8, 1),
        #    Placement(0.7, 0.8, 1)
        #)

