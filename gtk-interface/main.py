import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
from Services import MainService

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Raspberry Controller")
        self.set_default_size(800, 600)

        self.main_service = MainService()

        # Main container for the window
        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10,
            margin_top=20,
            margin_bottom=20,
            margin_start=25,
            margin_end=25
        )

        # Row 1

        button_row = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True,
            halign=Gtk.Align.FILL,
            spacing=10
        )

        label_button = Gtk.Label(label="Press this button to activate the LED")
        label_button.set_hexpand(True)
        label_button.set_halign(Gtk.Align.START)

        button = Gtk.Button(label="LED ON")
        button.connect("clicked", self.get_check_domain)

        button_row.append(label_button)
        button_row.append(button)

        box.append(button_row)

        # Row 2

        switch_row = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True,
            halign=Gtk.Align.FILL,
            spacing=10
        )

        label_switch = Gtk.Label(label="Switch to turn on/off the LED")
        label_switch.set_hexpand(True)
        label_switch.set_halign(Gtk.Align.START)

        switch = Gtk.Switch()
        switch.set_active(False)
        switch.connect("notify::active", self.main_service.on_switch_changed)
        
        switch_row.append(label_switch)
        switch_row.append(switch)

        box.append(switch_row)

        # Row Separator 

        separator = Gtk.Separator(
            orientation=Gtk.Orientation.HORIZONTAL
        )
        
        box.append(separator)

        # Row 3

        row_3 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True,
            halign=Gtk.Align.FILL,
            spacing=10
        )

        label_domain_name = Gtk.Label(label="Domain Name")
        label_domain_name.set_hexpand(True)
        label_domain_name.set_halign(Gtk.Align.START)

        self.entry_domain_name = Gtk.Entry()
        self.entry_domain_name.set_hexpand(True)
        self.entry_domain_name.set_halign(Gtk.Align.FILL)

        row_3.append(label_domain_name)
        row_3.append(self.entry_domain_name)

        box.append(row_3)

        # Row 4

        row_4 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True,
            halign=Gtk.Align.FILL,
            spacing=10
        )

        label_domain_info = Gtk.Label(label="Press this button to get domainInfo")
        label_domain_info.set_hexpand(True)
        label_domain_info.set_halign(Gtk.Align.START)

        button_domain_info = Gtk.Button(label="Domain Info")
        button_domain_info.connect("clicked", self.get_domain_info)

        row_4.append(label_domain_info)
        row_4.append(button_domain_info)

        box.append(row_4)

        # Row Separator 

        separator = Gtk.Separator(
            orientation=Gtk.Orientation.HORIZONTAL
        )

        box.append(separator)

        # Row 5

        row_5 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True,
            halign=Gtk.Align.FILL,
            spacing=10
        )

        self.text_box = Gtk.Entry()
        self.text_box.set_hexpand(True)
        self.text_box.set_halign(Gtk.Align.FILL)
        self.text_box.set_editable(False)

        row_5.append(self.text_box)

        box.append(row_5)

        # Assign all elements to the main window
        self.set_child(box)

    def get_domain_info(self, button):
        domain_name = self.entry_domain_name.get_text()
        
        def on_response(response):
            self.text_box.set_text(str(response))

        self.main_service.get_domain_info(domain_name, on_response)
        
    def get_check_domain(self, button):
        domain_name = self.entry_domain_name.get_text()
        print(domain_name)
        self.text_box.set_text(domain_name)

class MyApp(Gtk.Application):
    def do_activate(self):
        win = MainWindow(self)
        win.present()


app = MyApp()
app.run()
