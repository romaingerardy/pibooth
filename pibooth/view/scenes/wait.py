from pgi import require_version

from pibooth.view.scenes.paths import wait_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk, GLib, GObject, Gdk

from pibooth.view.scene import Scene, Placement
from pibooth.utils import LOGGER


class WaitScene(Scene):

    def __init__(self):
        super(WaitScene, self).__init__()
        LOGGER.info("new WaitScene")
        self._setup()

    def _setup(self):
        self.set_background(wait_media_path('blueprint-bg-4-3.png'),
                            wait_media_path('blueprint-bg-16-9.png'))

        self.add_widget(
            Gtk.Image.new_from_file(wait_media_path('shutdown_icon.png')),
            Placement(0.9, 0.9, 1),
            Placement(0.9, 0.9, 1)
        )

        self.add_widget(
            Gtk.Image.new_from_file(wait_media_path('wifi_icon.png')),
            Placement(0.8, 0.9, 1),
            Placement(0.8, 0.9, 1)
        )
