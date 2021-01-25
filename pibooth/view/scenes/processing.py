from pgi import require_version

from pibooth.view.scenes.paths import processing_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk, GdkPixbuf

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER


class ProcessingScene(Scene):
    app = None

    def __init__(self, app):
        super(ProcessingScene, self).__init__()
        LOGGER.info("new ProcessingScene")

        self.app = app
        self._setup()

    def _setup(self):
        self.set_background(processing_media_path('BG-Processing.png'),
                            processing_media_path('BG-Processing.png'))

        anim = GdkPixbuf.PixbufAnimation.new_from_file(processing_media_path('processing.gif'))

        self.add_widget(
            Gtk.Image.set_from_animation(anim),
            Placement(0.5, 0.5, 1),
            Placement(0.5, 0.5, 1)
        )
