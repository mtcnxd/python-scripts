import tkinter as tk
from MainWindow import MainWindow

container = tk.Tk()
container.title("Clients")
container.geometry("800x600")

MainWindow(container)

container.mainloop()
