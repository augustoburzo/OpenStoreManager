import sqlite3
from configparser import ConfigParser

class SQLiteVerify:
    """
    Strumento per verificare l'esistenza e l'integrità del database
    """
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("database.ini")
        self.database =  sqlite3.connect(self.config["database.settings"]["dbname"])
        self.db_cursor = self.database.cursor()
        # Creazione tabella Fidelity Card
        _SQL = """
CREATE TABLE IF NOT EXISTS "fidelity_card" (
	"id"	INTEGER NOT NULL UNIQUE,
	"id_cliente"	NUMERIC NOT NULL,
	"punteggio"	INTEGER,
	"credito"	NUMERIC,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
        self.db_cursor.execute(_SQL)

        # Creazione tabella Clienti
        _SQL = """
CREATE TABLE IF NOT EXISTS "customers" (
    "id" INTEGER NOT NULL UNIQUE,
    "nome_cliente"  TEXT,
    "cognome_cliente" TEXT,
    "telefono"  TEXT,
    "cellulare" TEXT,
    "email" TEXT,
    "indirizzo"    TEXT,
    "cap"   TEXT,
    "comune"    TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);
"""
        self.db_cursor.execute(_SQL)


if __name__ == "__main__":
    verify = SQLiteVerify()