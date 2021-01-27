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

        apply_colours_to_widget(self)

        self.internal_box = Gtk.Box(spacing=10)
        self.internal_box.props.halign = Gtk.Align.CENTER
        self.add(self.internal_box)

        if icon_filename:
            self.icon = Gtk.Image.new_from_file(icon_filename)
            self.internal_box.pack_start(self.icon, False, False, 0)
            self.label = Gtk.Label(text)
            self.internal_box.pack_start(self.label, False, False, 0)
        else:
            self.label = Gtk.Label(text)
            self.internal_box.add(self.label)

        #cursor.attach_cursor_events(self)

    def set_label(self, text):
        self.label.set_text(text)

    def get_label(self):
        return self.label.get_text()



class OrangeButton(GenericButton):
    BUTTON_CSS = os.path.join(common_css_dir, 'small_orange_button.css')

    def __init__(self, text=""):

        # Create button
        GenericButton.__init__(self, text)
        apply_styling_to_widget(self, self.BUTTON_CSS)
        apply_styling_to_widget(self.label, self.BUTTON_CSS)

        self.get_style_context().add_class("small_orange_button")

class PixButton(GenericButton):
    BUTTON_CSS = os.path.join(common_css_dir, 'pix_button.css')

    def __init__(self, text=""):

        # Create button
        GenericButton.__init__(self, text)
        apply_styling_to_widget(self, self.BUTTON_CSS)
        apply_styling_to_widget(self.label, self.BUTTON_CSS)

        self.get_style_context().add_class("pix_button")

