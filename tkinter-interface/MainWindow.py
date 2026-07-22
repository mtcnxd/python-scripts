from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from ApiClient import ApiClient
from FrameServiceDetails import FrameServiceDetails

class MainWindow(Frame):
    def __init__(self, container=None):
        super().__init__(container)
        self.master = container
        self.clients = []
        self.services = []
        self.listbox = Listbox(self.master, width=40)
        self.services_combobox = Combobox(self.master, width=38)
        self.id_string_var = StringVar()
        self.name_string_var = StringVar()
        self.phone_string_var = StringVar()
        self.email_string_var = StringVar()
        self.create_widgets()
        self.background_job()

    def background_job(self):
        print("Background job")
        self.after(500, self.background_job)

    def create_widgets(self):
        try:
            json_response = ApiClient().getAllClients()
            self.clients = json_response['data']
        
        except Exception as e:
            print(f"Error: {e}")

        Label(self.master, text="Clients").grid(row=0, column=0, sticky="n", padx=10, pady=10)

        for client in json_response['data']:
            self.listbox.insert(END, f"{client['id']} - {client['name']}")

        scrollbar = Scrollbar(self.master)
        scrollbar.grid(row=0, column=2, sticky="ns", pady=10)
        scrollbar.config(command=self.listbox.yview)

        self.listbox.grid(row=0, column=1, padx=10, pady=10)
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.func_on_select)

        Label(self.master, text="ID").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        Entry(self.master, width=40, textvariable=self.id_string_var).grid(row=1, column=1, padx=10, pady=10)

        Label(self.master, text="Name").grid(row=3, column=0, sticky="w", padx=10, pady=10)
        Entry(self.master, width=40, textvariable=self.name_string_var).grid(row=3, column=1, padx=10, pady=10)

        Label(self.master, text="Phone").grid(row=4, column=0, sticky="w", padx=10, pady=10)
        Entry(self.master, width=40, textvariable=self.phone_string_var).grid(row=4, column=1, padx=10, pady=10)

        Label(self.master, text="Email").grid(row=5, column=0, sticky="w", padx=10, pady=10)
        Entry(self.master, width=40, textvariable=self.email_string_var).grid(row=5, column=1, padx=10, pady=10)

        Label(self.master, text="Services").grid(row=6, column=0, sticky="w", padx=10, pady=10)
        self.services_combobox.grid(row=6, column=1, padx=10, pady=10)

        Button(self.master, text="Service Details", command=self.func_get_service_details).grid(row=7, column=1, padx=10, pady=10, sticky="w")

    def func_on_select(self, event):
        selected_index = self.listbox.curselection()

        if selected_index:
            index = selected_index[0]
            selected_client = self.clients[index]
            print(f"ID: {selected_client['id']} Name: {selected_client['name']}")
            self.func_show_client_details(selected_client)

    def func_show_client_details(self, client_data):
        try:
            json_response = ApiClient().getClientInfo(client_id=client_data['id'])
            self.func_get_services(client_data=client_data)
            
            self.id_string_var.set(json_response['data']['id'])
            self.name_string_var.set(json_response['data']['name'])
            self.phone_string_var.set(json_response['data']['phone'])
            self.email_string_var.set(json_response['data']['email'])
            
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showinfo("Error", f"Error: {e}")

    def func_get_services(self, client_data):        
        try:
            json_response = ApiClient().getClientServices(client_id=client_data['id'])
            count = len(json_response['data'])

            if count == 0:
                messagebox.showinfo("Services", "No services found")
                self.services = ["No services found"]
                return

            self.services = []
            for service in json_response['data']:
                self.services.append(f"{service['id']} - {service['car']} - {service['status']}")

            self.services_combobox.config(values=self.services)
        
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showinfo("Error", f"Error: {e}")

    def func_get_service_details(self):
        client_id = self.id_string_var.get()
        if not client_id:
            messagebox.showwarning("Warning", "Please select a client first")
            return

        popup = Toplevel()
        popup.title("Service Details")
        popup.resizable(False, False)
        popup.configure(padx=10, pady=10, width=710, height=400)
    
        FrameServiceDetails(popup, client_id)