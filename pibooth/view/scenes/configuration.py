from pgi import require_version

from pibooth.utils import LOGGER
from pibooth.view.scenes.paths import configuration_media_path, common_media_path

require_version('Gtk', '3.0')
from pgi.repository import Gtk

from pibooth.view.scene import Scene, Placement


class ConfigurationScene(Scene):

    def __init__(self, app, window):
        super(ConfigurationScene, self).__init__()
        self.app = app
        self.window = window
        self._setup()

    def _setup(self):
        self.set_background(configuration_media_path('BG-Configuration.png'),
                            configuration_media_path('BG-Configuration.png'))

        # Back icon
        self.add_widget(
            Gtk.Image.new_from_file(common_media_path('back-icon.png')),
            Placement(0.05, 0.05, 1),
            Placement(0.05, 0.05, 1),
            self._back
        )

        labelWifi = Gtk.Label("WiFi")
        labelSsid = Gtk.Label(str(self.app.wifi_ssid))
        LOGGER.info(str(self.app.wifi_ssid))

        self.add_widget(
            labelWifi,
            Placement(0.2, 0.1, 1),
            Placement(0.2, 0.1, 1)
        )

        self.add_widget(
            labelSsid,
            Placement(0.2, 0.2, 1),
            Placement(0.2, 0.2, 1)
        )

    def _back(self):
        self.window.hide_config()
