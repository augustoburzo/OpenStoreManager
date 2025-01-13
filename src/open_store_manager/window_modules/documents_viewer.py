import tkinter as tk
import ttkbootstrap as ttk

class DocumentsViewer(ttk.Toplevel):
    def __init__(self, win_title, *args, **kwargs):
        ttk.Toplevel.__init__(self, *args, **kwargs)
        self.geometry("800x600+100+100")
        self.title(win_title)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    module = DocumentsViewer(master=root, win_title="Gestione documenti")
    module.mainloop()
