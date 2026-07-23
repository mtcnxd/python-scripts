from tkinter import *

class MainWindow(Frame):
    def __init__(self, container=None):
        super().__init__(container)
        self.master = container
        self.create_widgets()

    def create_widgets(self):
        Button(self.master, text="LED ON", command=self.turn_on, height=20, width=30).grid(column=3, row=0, padx=10, pady=10)

        Button(self.master, text="LED OFF", command=self.turn_off, height=20, width=30).grid(column=4, row=0, padx=10, pady=10)

    def turn_on(self):
        print("LED On")

    def turn_off(self):
        print("LED Off")

    