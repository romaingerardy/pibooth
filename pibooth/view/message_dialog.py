import pgi

pgi.require_version("Gtk", "3.0")
from pgi.repository import Gtk


class MessageDialog(Gtk.MessageDialog):
    def __init__(self):

        super(MessageDialog, self).__init__(transient_for=self,
                                            flags=0,
                                            message_type=Gtk.MessageType.QUESTION,
                                            buttons=Gtk.ButtonsType.YES_NO,
                                            text="Eteindre")
        self.format_secondary_text(
            "Voulez-vous éteindre Pix Me Box ?"
        )
        response = self.run()
        if response == Gtk.ResponseType.YES:
            print("QUESTION dialog closed by clicking YES button")
        elif response == Gtk.ResponseType.NO:
            print("QUESTION dialog closed by clicking NO button")

        self.destroy()
