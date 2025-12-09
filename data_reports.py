import csv
from collections import defaultdict
from datetime import datetime

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

    print("=== Zusammenfassung ===")
    print(f"Einnahmen: {income:.2f} CHF")
    print(f"Ausgaben:  {expenses:.2f} CHF")
    print(f"Saldo: {income + expenses:.2f} CHF\n")
    

def show_largest_category(data: list[dict]):
    """Findet die Kategorie mit den höchsten Gesamtausgaben."""
    category_totals = defaultdict(float)

    for entry in data:
        betrag = entry["Betrag"]
        if betrag < 0:
            category_totals[entry["Kategorie"]] += betrag

        if not category_totals:
            print("Keine Ausgaben vorhanden.")
            return
        # Grösste Ausgabenkategorie (Betragmässig am meisten Minus)
        largest = min(category_totals, key=category_totals.get)

        print("=== Kategorie mit höchsten Ausgaben ===")
        print(f"{largest}: {category_totals[largest]:.2f} CHF\n")


def show_month_entries(data: list[dict], month: int, year: int):
    """Filtert Einträge nach Monat und Jahr und gibt sie tabellarisch aus."""
    filtered = []
    for e in data:
        m, y = parse_month_year(e["Datum"])
        if m == month and y == year:
            filtered.append(e)

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

if __name__ == "__main__":
    test_functions()
