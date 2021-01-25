from pgi import require_version

from pibooth.view.scenes.paths import common_media_path, choose_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk, GLib, GObject, Gdk

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER


class ChooseScene(Scene):
    app = None

    def __init__(self, app, choices):
        super(ChooseScene, self).__init__()
        LOGGER.info("new ChooseScene")
        self.app = app
        self._setup(choices)

    def _setup(self, choices):
        self.set_background(common_media_path('BG-Blank.png'),
                            common_media_path('BG-Blank.png'))

        LOGGER.info(choices)

        # Add choices
        if choices and len(choices) == 2:
            x = 0.25
            for choice in choices:
                self.add_widget(
                    Gtk.Image.new_from_file(choose_media_path('choice_po_' + str(choice) + '.png')),
                    Placement(x, 0.65, 1),
                    Placement(x, 0.65, 1),
                    self._chooseTemplate
                )
                x = x + 0.45
        elif choices and len(choices) == 1:
            self.add_widget(
                Gtk.Image.new_from_file(choose_media_path('choice_po_' + str(choices[0]) + '.png')),
                Placement(0.35, 0.65, 1),
                Placement(0.35, 0.65, 1),
                self._chooseTemplate
            )

    def _chooseTemplate(self):
        self.app.capture_nbr = 1
        self.app.goToChosenStep(1)