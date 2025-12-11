import csv
from collections import defaultdict
from datetime import datetime

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
                if name == "":
                    continue
                kategorien.append(name)
    except FileNotFoundError:
        
        print(f"Warnung: {filename} nicht gefunden. Datei wird neu erstellt.")
        return create_default_categories(filename)
 
    return kategorien

# Dateifunktionen

def get_budget_filename(month: int, year: int) -> str:
    """Erzeugt einen Dateinamen für das gegebene Jahr / Monat"""
    return f"budget_{year}_{month:02d}.csv"


def load_data(filename: str) -> list[dict]:
    """CSV-Datei lesen und jede Zeile als Dict zurückgeben."""
    data = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Betrag in float umwandeln
                row["Betrag"] = float(row["Betrag"])
                data.append(row)
    except FileNotFoundError:
        print(f"Datei {filename} nicht gefunden. Leere Liste wird zurückgegeben.")
    return data


def save_data(filename: str, data: list[dict]):
    """Liste von Dicts zurück in CSV schreiben."""
    if not data:
        print("Warnung: Keine Daten zum Speichern.")
        return
    with open(filename, mode="w", newline="",encoding="utf-8") as f:
        fieldnames = ["Datum", "Typ", "Kategorie", "Betrag"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# Hilfsfunktion, um Monat / Jahr aus Datum zu holen

def parse_month_year(datum_str: str) -> tuple[int, int]:
    """Erwartet Datum im Format TT.MM.JJJJ und gibt (Monat, Jahr) zurück."""
    try:
        dt = datetime.strptime(datum_str, "%d.%m.%Y")
        return dt.month, dt.year
    except ValueError:
        return 0, 0


# Auswertungsfunktionen

def show_summary(data: list[dict]):
    """Summiert Einnahmen, Ausgaben und berechnet den Saldo."""
    income = sum(entry["Betrag"] for entry in data if entry["Betrag"] > 0)
    expenses = sum(entry["Betrag"] for entry in data if entry["Betrag"] < 0)

    print("\n=== Zusammenfassung ===")
    print(f"Einnahmen: {income:.2f} CHF")
    print(f"Ausgaben:  {expenses:.2f} CHF")
    print(f"Saldo: {income + expenses:.2f} CHF\n")
    

def show_largest_category(data: list[dict]):
    """Findet die Kategorie mit den höchsten Gesamtausgaben."""
    expenses = [e for e in data if e ["Typ"] == "Ausgabe"]

    if not expenses:
        print("Keine Ausgaben vorhanden.")
        return
    
    # Summiere Ausgaben nach Kategorie 
    category_totals = {}
    for entry in expenses:
        category = entry["Kategorie"]
        amount = -entry["Betrag"] # Betrag positiv machen (war negativ gespeichert)
        category_totals[category] = category_totals.get(category, 0) + amount

    # Kategorie mit den höchstens Gesamtausgaben finden
    largest = max(category_totals, key=category_totals.get)
    
    print("=== Kategorie mit höchsten Ausgaben ===")
    print(f"{largest}: {category_totals[largest]:.2f} CHF\n")


def show_month_entries(data: list[dict], month: int, year: int):
    """Filtert Einträge nach Monat und Jahr und gibt sie tabellarisch aus."""
    filtered = [
        entry for entry in data
        if parse_month_year(entry["Datum"]) == (month, year)
    ]

    if not filtered:
        print("Keine Einträge für diesen Monat.")
        return    
    
    print(f"=== Einträge für {month:02d}/{year} ===")
    print(f"{'Datum':10} {'Typ':10} {'Kategorie':15} {'Betrag':>10}")
    print("-" * 50)

    for entry in filtered:
        print(f"{entry['Datum']:10} {entry['Typ']:10} {entry['Kategorie']:15} {entry['Betrag']:10.2f}")
    print()


# Testfunktion (Dummy-Daten)

def test_functions():
    test_data = [
        {"Datum": "01.05.2024", "Typ": "Ausgabe",  "Kategorie": "Essen",     "Betrag": -20.0},
        {"Datum": "02.05.2024", "Typ": "Einnahme", "Kategorie": "Gehalt",    "Betrag": 3500.0},
        {"Datum": "03.05.2024", "Typ": "Ausgabe",  "Kategorie": "Essen",     "Betrag": -15.0},
        {"Datum": "04.05.2024", "Typ": "Ausgabe",  "Kategorie": "Transport", "Betrag": -80.0},
     ]
    filename = get_budget_filename(5, 2024)

    save_data(filename, test_data)
    loaded = load_data(filename)

    show_summary(loaded)
    show_largest_category(loaded)
    show_month_entries(loaded, 5, 2024)
