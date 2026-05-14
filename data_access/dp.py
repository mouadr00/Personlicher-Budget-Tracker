from sqlmodel import SQLModel, create_engine, Session
# Models importieren von domain.models
from domain.models import User, Category, Transaction
#domain.models import User, Category, Transaction

# Dateiname defnieren für SQLite Datenbank
DATABASE_URL = "sqlite:///budget_tracker.db"

# Engine erstellen (create_engine)
# SQLite: echo=True hilft beim Debuggen, da es alle SQL-Befehle in der Konsole ausgibt
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    # Funktion erstellt Tabelle in der Datenbank.
    SQLModel.metadata.create_all(engine) #sollte am Anfang beim Programmstart ausgeführt werden

    pass

def get_session():
    # Funktion um neue Session zu erstellen für Datenbankabfragen zu erstellen
    # gibt Session(engine) zurück
    return Session(engine)
