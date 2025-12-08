from validationfunctions import *

# ============================================
#   Hauptfunktionen für Einnahmen & Ausgaben
# ============================================

def add_income(data, allowed_categories):
    """
    Fügt eine Einnahme zum Budget hinzu.
    Nutzt die Validierungsfunktionen.
    """
    print("\n--- Neue Einnahme ---")

    datum = input_date("Datum (TT.MM.JJJJ, leer = heute): ")
    kategorie = input_category("Kategorie: ", allowed_categories)
    betrag = input_amount("Betrag (+): ")

    eintrag = {
        "Datum": datum,
        "Typ": "Einnahme",
        "Kategorie": kategorie,
        "Betrag": betrag
    }
    data.append(eintrag)
    print("Einnahme gespeichert!\n")


def add_expense(data, allowed_categories):
    """
    Fügt eine Ausgabe zum Budget hinzu.
    Betrag wird automatisch negativ gespeichert.
    """
    print("\n--- Neue Ausgabe ---")

    datum = input_date("Datum (TT.MM.JJJJ, leer = heute): ")
    kategorie = input_category("Kategorie: ", allowed_categories)
    betrag = input_amount("Betrag (-): ")

    eintrag = {
        "Datum": datum,
        "Typ": "Ausgabe",
        "Kategorie": kategorie,
        "Betrag": -betrag
    }

    data.append(eintrag)
    print("Ausgabe gespeichert!\n")
