import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Hola mundo")
        self.set_default_size(800, 600)

        self.box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        button_row = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=10
        )

        button_row.label_button = Gtk.Label(label="Press this button to activate the LED")
        button_row.label_button.set_halign(Gtk.Align.START)
        button_row.append(button_row.label_button)

        button_row.button = Gtk.Button(label="LED ON")
        button_row.button.set_halign(Gtk.Align.END)
        button_row.button.set_valign(Gtk.Align.CENTER)
        button_row.button.connect("clicked", self.on_button_clicked)
        button_row.append(button_row.button)

        self.box.append(button_row)

        switch_row = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=10
        )

        switch_row.switch = Gtk.Switch()
        switch_row.switch.set_active(False)
        switch_row.switch.connect("notify::active", self.on_switch_changed)
        switch_row.append(switch_row.switch)

        self.box.append(switch_row)

        self.set_child(self.box)

    def on_button_clicked(self, button):
        print("Button clicked")

    def on_switch_changed(self, switch, gparam):
        if switch.get_active():
            print("Switch ON")
        else:
            print("Switch OFF")


class MyApp(Gtk.Application):
    def do_activate(self):
        win = MainWindow(self)
        win.present()


app = MyApp()
app.run()
