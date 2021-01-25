from pgi import require_version

from pibooth.view.scenes.paths import common_media_path, choose_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk, GLib, GObject, Gdk

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER


class ChosenScene(Scene):
    app = None

    def __init__(self, app, choices):
        super(ChosenScene, self).__init__()
        LOGGER.info("new ChosenScene")
        self.app = app
        self._setup(choices)

    def _setup(self, choice):
        self.set_background(common_media_path('BG-Blank.png'),
                            common_media_path('BG-Blank.png'))

        LOGGER.info(choice)

        # Summary of choice
        self.add_widget(
            Gtk.Image.new_from_file(choose_media_path('choice_po_' + str(choice) + '.png')),
            Placement(0.35, 0.65, 1),
            Placement(0.35, 0.65, 1)
        )
