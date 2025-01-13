import sqlite3
from configparser import ConfigParser


class CustomersManager:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("database.ini")
        if self.config["database.settings"]["type"] == "sqlite":
            self.database =  sqlite3.connect(self.config["database.settings"]["dbname"])
            self.db_cursor = self.database.cursor()
        else:
            raise NotImplementedError("Funzione non ancora implementata")

    def write_new_customer(self, nome, cognome, telefono, cellulare, email, indirizzo, cap, comune):
        if self.config["database.settings"]["type"] == "sqlite":
            _SQL = f"""
INSERT INTO "customers"(
    "nome_cliente",
    "cognome_cliente",
    "telefono", "cellulare",
    "email",
    "indirizzo",
    "cap",
    "comune") VALUES ("{nome}", "{cognome}", "{telefono}", "{cellulare}", "{email}", "{indirizzo}", "{cap}", "{comune}");        
"""
            self.db_cursor.execute(_SQL)
            self.database.commit()

    def load_customers(self):
        if self.config["database.settings"]["type"] == "sqlite":
            _SQL = "SELECT * FROM 'customers'"
            self.db_cursor.execute(_SQL)
            customers = self.db_cursor.fetchall()
            return customers