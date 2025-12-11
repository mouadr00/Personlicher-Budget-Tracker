from validationfunctions import *

from data_reports import get_budget_filename, load_data, save_data

# ============================================
#   Hauptfunktionen für Einnahmen & Ausgaben
# ============================================

def add_income(data, allowed_categories):
    """
    Fügt eine Einnahme zum Budget in der passenden Monatsdatei hinzu.
    Nutzt die Validierungsfunktionen.
    """
    print("\n--- Neue Einnahme ---")

    date = input_date("Datum (TT.MM.JJJJ) , leer = heute: ")
    category = input_category("Kategorie: ", allowed_categories)
    amount = input_amount("Betrag (+): ")

    # Monat/Jahr aus Datum extrahieren
    try:
        dt = datetime.strptime(date, "%d.%m.%Y")
        month, year = dt.month, dt.year
    except ValueError:
        print("Ungültiges Datum.")
        return

    # Daten für ensprechenden Monat laden
    filename = get_budget_filename(month, year)
    data = load_data(filename)

    entry = {
        "Datum": date,
        "Typ": "Einnahme",
        "Kategorie": category,
        "Betrag": amount # immer positiv speichern 
    }
   
    data.append(entry)
    save_data(filename, data)
    print("Einnahme gespeichert!\n")


def add_expense(data, allowed_categories):
    """
    Fügt eine Ausgabe zum Budget hinzu.
    Betrag wird automatisch negativ in der passenden Monatsdatei gespeichert.
    """
    print("\n--- Neue Ausgabe ---")

    date = input_date("Datum (TT.MM.JJJJ) , leer = heute: ")
    category = input_category("Kategorie: ", allowed_categories)
    amount = input_amount("Betrag (-): ")

    # Monat/Jahr aus Datum extrahieren
    try:
        dt = datetime.strptime(date, "%d.%m.%Y")
        month, year = dt.month, dt.year
    except ValueError:
        print("Ungültiges Datum.")
        return

    # Daten für ensprechenden Monat laden
    filename = get_budget_filename(month, year)
    data = load_data(filename)

    entry = {
        "Datum": date,
        "Typ": "Ausgabe",
        "Kategorie": category,
        "Betrag": amount # immer negativ speichern 
    }
    data.append(entry)
    save_data(filename, data)
    print("Ausgabe gespeichert!\n")
