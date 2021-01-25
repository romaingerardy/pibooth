#
# buttons.py
#
# Copyright (C) 2014 - 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPLv2
#
# Kano-styled buttons
#

import os

from pgi import require_version

require_version('Gtk', '3.0')

from pgi.repository import Gtk

from pibooth.common.apply_styles import apply_styling_to_widget, apply_colours_to_widget
from pibooth.common.common_paths import common_css_dir


class GenericButton(Gtk.Button):
    def __init__(self, text="", icon_filename=""):

        Gtk.Button.__init__(self)


    def set_label(self, text):
        self.label.set_text(text)

    def get_label(self):
        return self.label.get_text()

