from pgi import require_version

from pibooth.view.scenes.paths import preview_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER


class PreviewScene(Scene):
    app = None

    def __init__(self, app):
        super(PreviewScene, self).__init__()
        LOGGER.info("new PreviewScene")

        self.app = app
        self._setup()

    def _setup(self):
        self.set_background(preview_media_path('BG-Preview.png'),
                            preview_media_path('BG-Preview.png'))
        #self.text = Gtk.Label('TEST')
        #self.add_widget(
        #    self.text,
        #    Placement(0.5, 0.5, 1),
        #    Placement(0.5, 0.5, 1)
        #)

    def add_text(self, text):
        LOGGER.info(str(text))
        # Test add overlay
        if str(text) == '3':
            self.add_widget(
                Gtk.Image.new_from_file(preview_media_path('countdown_3.png')),
                Placement(0, 0, 1),
                Placement(0, 0, 1)
            )
        #self.text.set_text(str(text))
