import tkinter as tk
import ttkbootstrap as ttk
from tkinter.constants import *

from database_modules import CustomersManager


class CustomersViewer(ttk.Toplevel):
    def __init__(self, win_title, *args, **kwargs):
        ttk.Toplevel.__init__(self, *args, **kwargs)
        self.geometry("800x600+100+100")
        self.title(win_title)

        # Interfaccia principale
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=BOTH, expand=TRUE)
        self.customers_treeview = ttk.Treeview(self.main_frame, columns=("id", "nome", "cognome"), show="headings")
        self.customers_treeview.heading("#0", text="ID")
        self.customers_treeview.heading("id", text="ID")
        self.customers_treeview.column("id", width=5, minwidth=5)
        self.customers_treeview.heading("nome", text="Nome")
        self.customers_treeview.column("nome", minwidth=10, width=10)
        self.customers_treeview.heading("cognome", text="Cognome")
        self.customers_treeview.column("cognome", minwidth=10, width=10)
        self.customers_treeview.grid(column=0, row=0, sticky=NSEW)
        self.customer_edit_labelframe = ttk.Labelframe(self.main_frame, text="Modifica cliente")
        self.customer_edit_labelframe.grid(column=1, row=0, sticky=NSEW)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=3)
        self.main_frame.rowconfigure(0, weight=1)

        # Toolbar
        self.toolbar_frame = ttk.Frame(self)
        self.toolbar_frame.pack(fill=X)
        self.add_customer_button = ttk.Button(self.toolbar_frame,
                                              text="Aggiungi cliente")
        self.add_customer_button.grid(column=0, row=0, pady=5, padx=1)

        # Status bar
        self.status_bar = ttk.Label(self, text="Pronto...")
        self.status_bar.pack(fill=X, anchor=S)

        self.on_load()

    def set_status(self, status):
        self.status_bar.configure(text=status)

    def on_load(self):
        db_util = CustomersManager()
        customers = db_util.load_customers()
        for customer in customers:
            self.customers_treeview.insert("", END, values=(customer[0], customer[1], customer[2]))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    module = CustomersViewer(master=root, win_title="Gestione clienti")
    module.mainloop()
