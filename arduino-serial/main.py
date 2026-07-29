import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk, GLib, Notify
from Services import SerialPort

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Arduino Serial Port")
        self.set_default_size(800, 600)
        self.store_enabled = False
        self.counter = 0

        # Main container for the window
        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10,
            margin_top=20,
            margin_bottom=20,
            margin_start=25,
            margin_end=25
        )

        # Row 0

        row_0 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True,
            halign=Gtk.Align.FILL,
            spacing=10
        )

        label_baudrate = Gtk.Label(label="Select baudrate and click on connect button")
        label_baudrate.set_hexpand(True)
        label_baudrate.set_halign(Gtk.Align.START)

        list_values = [
            "9600",
            "115200"
        ]

        self.baudrate_dropdown = Gtk.DropDown.new_from_strings(list_values)
        self.baudrate_dropdown.connect("notify::active", self.store_data)

        button_connect = Gtk.Button(label="Connect")
        button_connect.connect("clicked", self.connect)
        
        row_0.append(label_baudrate)
        row_0.append(self.baudrate_dropdown)
        row_0.append(button_connect)

        box.append(row_0)

        # Row Separator 

        separator = Gtk.Separator(
            orientation=Gtk.Orientation.HORIZONTAL
        )
        
        box.append(separator)

        # Row 1

        row_1 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True,
            halign=Gtk.Align.FILL,
            spacing=10
        )

        label_switch = Gtk.Label(label="Enable store data")
        label_switch.set_hexpand(True)
        label_switch.set_halign(Gtk.Align.START)

        switch = Gtk.Switch()
        switch.set_active(False)
        switch.connect("notify::active", self.store_data)
        
        row_1.append(label_switch)
        row_1.append(switch)

        box.append(row_1)

        # Row 2

        row_2 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True,
            halign=Gtk.Align.FILL,
            spacing=10
        )

        label_value_read = Gtk.Label(label="Value read: ")
        label_value_read.set_hexpand(True)
        label_value_read.set_halign(Gtk.Align.START)

        self.entry_value_read = Gtk.Entry()
        self.entry_value_read.set_hexpand(True)
        self.entry_value_read.set_halign(Gtk.Align.FILL)

        row_2.append(label_value_read)
        row_2.append(self.entry_value_read)

        box.append(row_2)

        row_3 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True,
            halign=Gtk.Align.END,
            spacing=10
        )

        button_start = Gtk.Button(label="Start")
        button_start.connect("clicked", self.start)

        button_cancel = Gtk.Button(label="Cancel")
        button_cancel.connect("clicked", self.cancel)

        row_3.append(button_start)
        row_3.append(button_cancel)

        box.append(row_3)

        # Assign all elements to the main window
        self.set_child(box)

    def connect(self, button):
        item = self.baudrate_dropdown.get_selected_item()
        baudrate = int(item.get_string())

        try:
            # Start arduino service
            self.serial_port = SerialPort()
            self.serial_port.connect(port="/dev/ttyUSB0", baudrate=baudrate)
            Gtk.AlertDialog(
                message="Success",
                detail="Arduino connected successfully",
            ).show()

        except Exception as e:
            Notify.init("Arduino Serial")

            notification = Notify.Notification.new(
                "Port not found",
                "Error al conectar con Arduino",
                "dialog-error"
            )
            notification.show()

            Gtk.AlertDialog(
                message="Port not found",
                detail=f"Error: {e}"
            ).show()

    def background_job(self):
        try:
            data = self.serial_port.get_data()

            if data:
                count = str(data[0])
                value = str(data[1])

                # Print values
                self.entry_value_read.set_text(value)

                # Save data
                if self.store_enabled:
                    self.serial_port.save_data(count, value)

            GLib.timeout_add(100, self.background_job)
        
        except Exception as e:
            print(f"Error: {e}")

            Gtk.AlertDialog(
                message="An error was ocurred",
                detail=f"Error: {e}"
            ).show()

    def store_data(self, switch, pspec):
        print(f"Store data: {switch.get_active()}")
        self.store_enabled = switch.get_active()

    def start(self, button):
        if self.serial_port:
            self.serial_port.send_data("A")
            self.background_job()

    def cancel(self, button):
        if self.serial_port:
            self.serial_port.send_data("B")

class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.ArduinoSerialPort")

    def do_activate(self):
        win = MainWindow(self)
        win.present()


app = MyApp()
app.run()