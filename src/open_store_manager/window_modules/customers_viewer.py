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
        self.customers_treeview.grid(column=0, row=0, sticky=NSEW, padx=5, pady=5)
        self.customer_edit_labelframe1 = ttk.Labelframe(self.main_frame, text="Modifica cliente")
        self.customer_edit_labelframe1.grid(column=1, row=0, sticky=NSEW, padx=5, pady=5, ipadx=5)
        self.customer_edit_labelframe = ttk.Frame(self.customer_edit_labelframe1)
        self.customer_edit_labelframe.pack(padx=5, pady=5, fill=BOTH, expand=TRUE)
        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Maschera inserimento
        self.customer_id_lbl = ttk.Label(self.customer_edit_labelframe, text="ID Cliente:")
        self.customer_id_lbl.grid(column=0, row=0, sticky=E)
        self.customer_id_entry = ttk.Entry(self.customer_edit_labelframe)
        self.customer_id_entry.grid(column=1, row=0, sticky=EW)
        self.customer_first_name_lbl = ttk.Label(self.customer_edit_labelframe, text="Nome:")
        self.customer_first_name_lbl.grid(column=0, row=1, sticky=E)
        self.customer_first_name_entry = ttk.Entry(self.customer_edit_labelframe)
        self.customer_first_name_entry.grid(column=1, row=1, sticky=EW)
        self.customer_last_name_lbl = ttk.Label(self.customer_edit_labelframe, text="Cognome:")
        self.customer_last_name_lbl.grid(column=2, row=1, sticky=E)
        self.customer_last_name_entry = ttk.Entry(self.customer_edit_labelframe)
        self.customer_last_name_entry.grid(column=3, row=1, sticky=EW)
        self.customer_phone_lbl = ttk.Label(self.customer_edit_labelframe, text="Telefono:")
        self.customer_phone_lbl.grid(column=0, row=2, sticky=E)
        self.customer_phone_entry = ttk.Entry(self.customer_edit_labelframe)
        self.customer_phone_entry.grid(column=1, row=2, columnspan=3, sticky=EW)
        self.customer_cellular_lbl = ttk.Label(self.customer_edit_labelframe, text="Cellulare:")
        self.customer_cellular_lbl.grid(column=0, row=3, sticky=E)
        self.customer_cellular_entry = ttk.Entry(self.customer_edit_labelframe)
        self.customer_cellular_entry.grid(column=1, row=3, columnspan=3, sticky=EW)
        self.customer_email_lbl = ttk.Label(self.customer_edit_labelframe, text="Email:")
        self.customer_email_lbl.grid(column=0, row=4, sticky=E)
        self.customer_email_entry = ttk.Entry(self.customer_edit_labelframe)
        self.customer_email_entry.grid(column=1, row=4, columnspan=3, sticky=EW)
        self.customer_address_lbl = ttk.Label(self.customer_edit_labelframe, text="Indirizzo:")
        self.customer_address_lbl.grid(column=0, row=5, sticky=E)
        self.customer_address_entry = ttk.Entry(self.customer_edit_labelframe)
        self.customer_address_entry.grid(column=1, row=5, columnspan=3, sticky=EW)
        self.customer_city_lbl = ttk.Label(self.customer_edit_labelframe, text="Comune:")
        self.customer_city_lbl.grid(column=0, row=6, sticky=E)
        self.customer_city_entry = ttk.Entry(self.customer_edit_labelframe)
        self.customer_city_entry.grid(column=1, row=6, sticky=EW)
        self.customer_zip_lbl = ttk.Label(self.customer_edit_labelframe, text="CAP:")
        self.customer_zip_lbl.grid(column=2, row=6, sticky=E)
        self.customer_zip_entry = ttk.Entry(self.customer_edit_labelframe)
        self.customer_zip_entry.grid(column=3, row=6, sticky=EW)
        self.customer_notes_lbl = ttk.Label(self.customer_edit_labelframe, text="Note:")
        self.customer_notes_lbl.grid(column=0, row=7, sticky=E)
        self.customer_notes_text = ttk.Text(self.customer_edit_labelframe, height=5, width=20)
        self.customer_notes_text.grid(column=1, row=7, columnspan=4, sticky=EW)

        self.customer_edit_labelframe.columnconfigure(1, weight=1)
        self.customer_edit_labelframe.columnconfigure(3, weight=1)

        rows = self.customer_edit_labelframe.grid_size()[1]
        while rows >= 0:
            self.customer_edit_labelframe.rowconfigure(rows, weight=1)
            rows -= 1

        # Toolbar
        self.toolbar_frame = ttk.Frame(self)
        self.toolbar_frame.pack(fill=X)
        self.add_customer_button = ttk.Button(self.toolbar_frame,
                                              text="Aggiungi cliente")
        self.add_customer_button.grid(column=0, row=0, pady=5, padx=1)
        self.export_customers_list_button = ttk.Button(self.toolbar_frame,
                                                       text="Esporta lista clienti")
        self.export_customers_list_button.grid(column=1, row=0, pady=5, padx=1)

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
