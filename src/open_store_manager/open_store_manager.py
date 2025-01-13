import tkinter as tk

import darkdetect
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from ttkbootstrap.constants import *

from resources.constants import *
from window_modules import DocumentsViewer, FidelityCardViewer, DeliveriesViewer


class OpenStoreManager(ttk.Window):
    def __init__(self, *args, **kwargs):
        ttk.Window.__init__(self, *args, **kwargs)
        self.geometry("1024x768+100+0")
        self.title(f"{FORMAL_NAME} - {VERSION}")

        # Menu Bar
        self.main_menu = tk.Menu(self, tearoff=FALSE)
        self.file_menu = tk.Menu(self.main_menu, tearoff=FALSE)
        self.edit_menu = tk.Menu(self.main_menu, tearoff=FALSE)
        self.about_menu = tk.Menu(self.main_menu, tearoff=FALSE)

        # File menu
        self.file_menu.add_command(label="Export...")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.destroy)

        # Add everything to menu
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.main_menu.add_cascade(label="?", menu=self.about_menu)
        self.configure(menu=self.main_menu)

        # Top Bar
        self.top_bar_frame = ttk.Frame(self)
        self.top_bar_frame.pack(fill=X)
        self.fidelity_image = ImageTk.PhotoImage(Image.open("resources/assets/card.png"))
        self.fidelity_button = ttk.Button(self.top_bar_frame,
                                          text="Fidelity card",
                                          compound=LEFT, image=self.fidelity_image,
                                          command=self.open_fidelity_card_window)
        self.fidelity_button.grid(column=0, row=0, padx=1)
        self.cash_register_image = ImageTk.PhotoImage(Image.open("resources/assets/cash_register.png"))
        self.cash_register_button = ttk.Button(self.top_bar_frame,
                                               text="Flussi cassa",
                                               compound=LEFT, image=self.cash_register_image)
        self.cash_register_button.grid(column=1, row=0, padx=1)
        self.delivery_image = ImageTk.PhotoImage(Image.open("resources/assets/delivery.png"))
        self.delivery_button = ttk.Button(self.top_bar_frame,
                                          text="Consegne",
                                          compound=LEFT, image=self.delivery_image,
                                          command=self.open_deliveries_window)
        self.delivery_button.grid(column=2, row=0, padx=1)
        self.vertical_separator = ttk.Separator(self.top_bar_frame, orient=VERTICAL)
        self.vertical_separator.grid(column=3, row=0, padx=1)
        self.documents_image = ImageTk.PhotoImage(Image.open("resources/assets/document.png"))
        self.documents_button = ttk.Button(self.top_bar_frame,
                                           text="Documenti",
                                           compound=LEFT, image=self.documents_image,
                                           command=self.open_documents_window)
        self.documents_button.grid(column=4, row=0, padx=1)

        # Dashboard
        self.dashboard_label_frame = ttk.LabelFrame(self, text="Dashboard")
        self.dashboard_label_frame.pack(fill=BOTH, expand=TRUE, padx=5, pady=5)
        self.notebook = ttk.Notebook(self.dashboard_label_frame)
        self.notebook.pack(fill=BOTH, expand=TRUE, padx=5, pady=5)
        self.documents_dashboard = ttk.Frame(self.notebook)
        self.notebook.add(self.documents_dashboard, text="Documenti")
        self.delivery_dashboard = ttk.Frame(self.notebook)
        self.notebook.add(self.delivery_dashboard, text="Consegne")
        self.agenda_dashboard = ttk.Frame(self.notebook)
        self.notebook.add(self.agenda_dashboard, text="Agenda")

        # Shortcuts bar
        self.shortcuts_bar = ttk.Frame(self, style=PRIMARY)
        self.shortcuts_bar.pack(fill=X)
        self.plus24_image = ImageTk.PhotoImage(Image.open("resources/assets/plus24.png"))
        self.add_document_button = ttk.Button(self.shortcuts_bar,
                                              text="Aggiungi documento",
                                              compound=LEFT, image=self.plus24_image, style=LIGHT)
        self.add_document_button.grid(column=0, row=0, padx=1, pady=5)
        self.schedule24_image = ImageTk.PhotoImage(Image.open("resources/assets/schedule24.png"))
        self.add_delivery_button = ttk.Button(self.shortcuts_bar,
                                              text="Aggiungi consegna",
                                              compound=LEFT, image=self.schedule24_image, style=LIGHT)
        self.add_delivery_button.grid(column=1, row=0, padx=1, pady=5)

        # Status bar
        self.status_bar = ttk.Label(self, text="Pronto...", relief=SUNKEN)
        self.status_bar.pack(fill=X, anchor=S)

    def open_documents_window(self):
        win = DocumentsViewer(master=self, win_title=f"{FORMAL_NAME} - Gestione documenti")
        win.focus_set()

    def open_fidelity_card_window(self):
        win = FidelityCardViewer(master=self, win_title=f"{FORMAL_NAME} - Gestione fidelity card")
        win.focus_set()

    def open_deliveries_window(self):
        win = DeliveriesViewer(master=self, win_title=f"{FORMAL_NAME} - Gestione consegne")
        win.focus_set()

    def set_status(self, status):
        self.status_bar.configure(text=status)


if __name__ == "__main__":
    theme = "flatly"
    if darkdetect.isDark():
        theme = "flatly"
    elif darkdetect.isLight():
        theme = "litera"
    app = OpenStoreManager(themename=theme)
    app.mainloop()
