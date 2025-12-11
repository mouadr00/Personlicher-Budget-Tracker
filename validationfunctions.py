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

def create_default_categories(filename: str = "kategorien.csv") -> list[str]:
    """
    Erstellt die Datei kategorien.csv mit Standardkategorien,
    wenn sie nicht existiert.
    """
    default_categories = [
        "Lebensmittel",
        "Gehalt",
        "Miete",
        "Versicherung",
        "Freizeit",
        "Transport",
        "Sparen",
        "Schulden",
        "Sonstiges"   
    ]
 
    with open(filename, mode="w", encoding="utf-8", newline="") as f:
        import csv
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Kategorie"])
        for cat in default_categories:
            writer.writerow([cat])
 
    print(f"{filename} wurde mit Standardkategorien erstellt.")

    return default_categories

def load_categories(filename: str = "kategorien.csv") -> list[str]:
    """
    Liest die Kategorien aus kategorien.csv.
    Falls die Datei fehlt, wird sie automatisch mit Standardwerten erstellt.
    """
    kategorien: list[str] = []
    try:
        with open(filename, mode="r", encoding="utf-8", newline="") as f:
            import csv
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                if not row:
                    continue
                name = row[0].strip()
                
                # Kopfzeile "Kategorie" überspringen
                if name.lower() == "kategorie" or name == "":
                    continue
                kategorien.append(name)
    except FileNotFoundError:
        
        print(f"Warnung: {filename} nicht gefunden. Datei wird neu erstellt.")
        return create_default_categories(filename)
 
    return kategorien
