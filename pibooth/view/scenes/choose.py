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
                self._addTemplateChoice(choice, x)
                x = x + 0.45
        elif choices and len(choices) == 1:
            self.add_widget(
                Gtk.Image.new_from_file(choose_media_path('choice_po_' + str(choices[0]) + '.png')),
                Placement(0.5, 0.65, 1),
                Placement(0.5, 0.65, 1),
                self._chooseTemplate
            )

    def _addTemplateChoice(self, nb, x):
        if nb == 1:
            self.add_widget(
                Gtk.Image.new_from_file(choose_media_path('choice_po_1.png')),
                Placement(x, 0.65, 1),
                Placement(x, 0.65, 1),
                self._chooseTemplate
            )
        elif nb == 2:
            self.add_widget(
                Gtk.Image.new_from_file(choose_media_path('choice_po_2.png')),
                Placement(x, 0.65, 1),
                Placement(x, 0.65, 1),
                self._chooseTemplate
            )
        elif nb == 3:
            self.add_widget(
                Gtk.Image.new_from_file(choose_media_path('choice_po_3.png')),
                Placement(x, 0.65, 1),
                Placement(x, 0.65, 1),
                self._chooseTemplate
            )
        elif nb == 4:
            self.add_widget(
                Gtk.Image.new_from_file(choose_media_path('choice_po_4.png')),
                Placement(x, 0.65, 1),
                Placement(x, 0.65, 1),
                self._chooseTemplate
            )
        elif nb == 8:
            self.add_widget(
                Gtk.Image.new_from_file(choose_media_path('choice_po_8.png')),
                Placement(x, 0.65, 1),
                Placement(x, 0.65, 1),
                self._chooseTemplate
            )

    def _chooseTemplate_1(self):
        self.app.capture_nbr = 1
        self.app.goToChosenStep(1)

    def _chooseTemplate_2(self):
        self.app.capture_nbr = 2
        self.app.goToChosenStep(2)

    def _chooseTemplate_3(self):
        self.app.capture_nbr = 3
        self.app.goToChosenStep(3)

    def _chooseTemplate_4(self):
        self.app.capture_nbr = 4
        self.app.goToChosenStep(4)

    def _chooseTemplate_8(self):
        self.app.capture_nbr = 8
        self.app.goToChosenStep(8)

    def _chooseTemplate(self, nb=1):
        self.app.capture_nbr = nb
        self.app.goToChosenStep(nb)