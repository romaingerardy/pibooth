# -*- coding: utf-8 -*-

"""Pibooth view management.
"""

from pgi import require_version

from pibooth.common.apply_styles import apply_common_to_screen
from pibooth.utils import LOGGER
from pibooth.view import background
from pibooth.view.scene import Scene
from pibooth.view.scenes.choose import ChooseScene
from pibooth.view.scenes.chosen import ChosenScene
from pibooth.view.scenes.preview import PreviewScene
from pibooth.view.scenes.processing import ProcessingScene
from pibooth.view.scenes.share import ShareScene
from pibooth.view.scenes.wait import WaitScene

require_version('Gtk', '3.0')
from pgi.repository import Gtk, GLib, Gdk


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

        self._print_number = 0
        self._print_failure = False
        self._capture_number = (0, 4)  # (current, max)

        # self._ctl = DesktopController(self)
        self.connect("delete-event", Gtk.main_quit)
        self._child = None

        self._press_signal_id = None
        self._release_signal_id = None
        self._emergency_counter = 0

        self._to_id_counter = 0
        self._timeouts = []

        self.preview_scene = None

        apply_common_to_screen()
        # apply_styling_to_screen(init_flow_css_path('scene.css'))

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

        emergency_exit = Gtk.EventBox()
        emergency_exit.set_halign(Gtk.Align.START)
        emergency_exit.set_valign(Gtk.Align.START)
        emergency_exit.set_size_request(20, 20)
        emergency_exit.connect('button-release-event', self._emergency_exit_cb)
        overlay.add_overlay(emergency_exit)

        self.connect('key-release-event', self._key_emergency_exit)
        self.connect('key-release-event', self._key_skip_stage)

        debug_button = Gtk.EventBox()
        debug_button.add(Gtk.Label('Fermer'))
        debug_button.set_halign(Gtk.Align.END)
        debug_button.set_valign(Gtk.Align.START)
        debug_button.connect('button-release-event', Gtk.main_quit)
        overlay.add_overlay(debug_button)

    def push(self, child):
        GLib.idle_add(self._do_push, child)

    def set_print_number(self, current_nbr=None, failure=None):
        """Set the current number of tasks in the printer queue.
        """
        LOGGER.info("set_print_number no code...")

    def _do_push(self, child):
        # Cleans up any pending scheduled events
        for i, src in enumerate(self._timeouts):
            del self._timeouts[i]
            # print GLib.source_remove_by_funcs_user_data(src.source_funcs,
            #                                            src.callback_data)
            # src.destroy()
            # if not src.is_destroyed():
            #    GLib.source_remove(src.get_id())

        if issubclass(child.__class__, Scene):
            for event in child.scheduled_events:
                self.schedule_event(event)

            child.set_active()
            child = child.widget

        if self._child:
            self._container.remove(self._child)
            self._child.destroy()

        self._child = child
        self._container.add(child)
        child.show_all()
        return False

    def _key_emergency_exit(self, widget, event):
        if (hasattr(event, 'keyval') and
                event.keyval in [Gdk.KEY_Q, Gdk.KEY_q] and
                event.state & Gdk.ModifierType.SHIFT_MASK and
                event.state & Gdk.ModifierType.CONTROL_MASK):
            self._emergency_exit_cb(widget)

        return False

    def _key_skip_stage(self, widget, event):
        if (hasattr(event, 'keyval') and
                event.keyval in [Gdk.KEY_N, Gdk.KEY_n] and
                event.state & Gdk.ModifierType.SHIFT_MASK and
                event.state & Gdk.ModifierType.CONTROL_MASK):
            LOGGER.info("Next Stage...")
            # self._ctl.next_stage()

    def _emergency_exit_cb(self, widget, data=None):
        self._emergency_counter += 1
        msg = "Emergency button pressed {}x".format(self._emergency_counter)
        # logger.warn(msg)
        print(msg)
        if self._emergency_counter >= self.EMERGENCY_EXIT_CLICKS:
            # logger.warn("Emergency exiting the init flow")
            print("Emergency exiting the init flow")
            # self._ctl.complete()
            Gtk.main_quit()
        else:
            Gtk.main_quit()

    def drop_cache(self):
        """Drop all cached background and foreground to force
        refreshing the view.
        """
        self._current_background = None
        self._current_foreground = None
        self._buffered_images = {}

    def show_oops(self):
        """Show failure view in case of exception.
        """
        LOGGER.error("OOPS !! erreur")
        self._capture_number = (0, self._capture_number[1])
        # self._update_background(background.OopsBackground())

    def show_intro(self, pil_image=None, with_print=True):
        """Show introduction view.
        """
        LOGGER.info("show_intro")
        scene = WaitScene(self.app)
        self.push(scene)

    def show_image(self, pil_image=None, pos=CENTER):
        """Show PIL image as it (no resize).
        """
        LOGGER.info("show_image")


    @property
    def return_value(self):
        return 1  # self._ctl.return_value
