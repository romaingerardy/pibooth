# -*- coding: utf-8 -*-

"""Pibooth view management.
"""

from pgi import require_version

from pibooth.utils import LOGGER
from pibooth.view import background

require_version('Gtk', '3.0')
from pgi.repository import Gtk, Gdk


class MyDialog(Gtk.Window):
    EMERGENCY_EXIT_CLICKS = 5
    width = 1024  # 1920
    height = 600  # 1080

    CENTER = 'center'
    RIGHT = 'right'
    LEFT = 'left'

    app = None

    def __init__(self, app,
                 title,
                 size=(800, 480),
                 color=(0, 0, 0),
                 text_color=(255, 255, 255),
                 arrow_location=background.ARROW_BOTTOM,
                 arrow_offset=0,
                 debug=False):

        super(MyDialog, self).__init__()

        LOGGER.info("MyDialog")

        self.app = app
        self.__size = size
        self.debug = debug
        self.bg_color = color
        self.text_color = text_color
        self.arrow_location = arrow_location
        self.arrow_offset = arrow_offset

        self.connect("delete-event", Gtk.main_quit)
        self._child = None

        self._press_signal_id = None
        self._release_signal_id = None
        self._emergency_counter = 0

        self._to_id_counter = 0
        self._timeouts = []

        self.set_decorated(False)

        screen = Gdk.Screen.get_default()
        width = screen.get_width()
        height = screen.get_height()
        self.set_size_request(width, height + 1)
        self.set_position(Gtk.WindowPosition.CENTER)

        overlay = Gtk.Overlay()
        self._child = Gtk.EventBox()
        overlay.add(self._child)
        self.add(overlay)
        self._container = overlay
        self._container.set_halign(Gtk.Align.CENTER)
        self._container.set_valign(Gtk.Align.CENTER)

    @property
    def return_value(self):
        return 1  # self._ctl.return_value
