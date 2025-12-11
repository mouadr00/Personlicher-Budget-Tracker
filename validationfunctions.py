from datetime import datetime

import csv

# ============================================
#   Validierungsfunktionen
# ============================================

def input_date(prompt):
    """
    Fragt ein Datum im Format TT.MM.JJJJ ab.
    Leere Eingabe -> heutiges Datum.
    Prüft Format mit try/except.
    """
    while True:
        value = input(prompt).strip()

        if value == "":
            return datetime.now().strftime("%d.%m.%Y")

        try:
            datetime.strptime(value, "%d.%m.%Y")
            return value
        except ValueError:
            print("Ungültiges Datum! Bitte TT.MM.JJJJ eingeben.")
    


def input_amount(prompt):
    """
    Fragt einen Betrag ab:
    - muss Zahl sein
    - max. 2 Nachkommastellen
    - nicht negativ (für Eingabe)
    """
    while True:
        value = input(prompt).replace(",", ".").strip()

        try:
            amount = float(value)

            # Prüfen auf max. 2 Nachkommastellen
            if "." in value:
                decimals = value.split(".")[1]
                if len(decimals) > 2:
                    print("Maximal 2 Nachkommastellen erlaubt.")
                    continue

            if amount < 0:
                print("Bitte eine positive Zahl eingeben.")
                continue

            return amount

        except ValueError:
            print("Ungültige Zahl!")
        except IndexError:
            print("Ungültiges Zahlenformat!")

def input_category(prompt, allowed_categories):
    """
    Fragt eine Kategorie ab.
    Nur erlaubte Kategorien sind gültig.
    """
    print("Erlaubte Kategorien:", ", ".join(allowed_categories))
    
    while True:
        value = input(prompt).strip().title()

        if value in allowed_categories:
            return value
        else:
            print("Kategorie nicht erlaubt! Bitte erneut eingeben.")

def load_categories(filepath: str) -> list[str]:
    """Lädt erlaubte Kategorien aus einer CSV-Datei."""
    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            return [row[0] for row in reader if row]
    except FileNotFoundError:
        print(f" Datei nicht gefunden: {filepath}")
        return []
