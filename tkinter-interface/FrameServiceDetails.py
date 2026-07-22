from tkinter import *
from tkinter import messagebox
from ApiClient import ApiClient

class FrameServiceDetails(Frame):
    def __init__(self, master=None, client_id=None):
        super().__init__(master)
        self.master = master
        self.client_id = client_id
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        # Get service details from API
        client_info = self.get_client_info(self.client_id)

        if not client_info:
            messagebox.showinfo("Error", "Could not retrieve client details")
            return

        Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        name_var = StringVar()
        name_var.set(client_info.get('name',''))
        Entry(self, textvariable=name_var, width=40).grid(row=0, column=1)
        
        Label(self, text="Phone:").grid(row=0, column=2, padx=10, pady=5)
        phone_var = StringVar()
        phone_var.set(client_info.get('phone'))
        Entry(self, textvariable=phone_var, width=40).grid(row=0, column=3)

        Label(self, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        email_var = StringVar()
        email_var.set(client_info.get('email'))
        Entry(self, textvariable=email_var, width=40).grid(row=2, column=1)
        
    def get_client_info(self, client_id):
        try:
            json_response = ApiClient().getClientInfo(client_id)
            return json_response['data']

        except Exception as e:
            print(f"API Error: {e}")
            return None
            