import tkinter as tk
from Views.MainWindow import MainWindow

container = tk.Tk()
container.title("Bitso Price")
container.geometry("800x600")

MainWindow(container)

container.mainloop()
