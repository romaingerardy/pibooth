from pgi import require_version

from pibooth.common.apply_styles import apply_styling_to_widget
from pibooth.common.buttons import PixButton
from pibooth.utils import LOGGER
from pibooth.view.scenes.paths import configuration_media_path, common_media_path, configuration_css_path

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

        apply_styling_to_widget(labelWifi, configuration_css_path('configuration.css'))
        apply_styling_to_widget(labelSsid, configuration_css_path('configuration.css'))
        labelWifi.get_style_context().add_class("title")
        labelSsid.get_style_context().add_class("item")

        self.add_widget(
            labelWifi,
            Placement(0.05, 0.3, 1),
            Placement(0.05, 0.3, 1)
        )

        self.add_widget(
            labelSsid,
            Placement(0.2, 0.3, 1),
            Placement(0.2, 0.3, 1)
        )

    def _putUpdateButtons(self):
        update_button = PixButton('Chercher des mises à jour')
        sync_button = PixButton('Synchroniser')
        self.add_widget(
            update_button,
            Placement(0.05, 0.5, 1),
            Placement(0.05, 0.5, 1)
        )
        self.add_widget(
            sync_button,
            Placement(0.05, 0.6, 1),
            Placement(0.05, 0.6, 1)
        )

    def _back(self):
        self.window.hide_config()
