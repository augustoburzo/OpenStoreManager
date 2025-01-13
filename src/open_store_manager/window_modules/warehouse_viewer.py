import tkinter as tk
import ttkbootstrap as ttk

class WarehouseViewer(ttk.Toplevel):
    def __init__(self, win_title, *args, **kwargs):
        ttk.Toplevel.__init__(self, *args, **kwargs)
        self.geometry("800x600+100+100")
        self.title(win_title)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    module = WarehouseViewer(master=root, win_title="Gestione magazzino")
    module.mainloop()