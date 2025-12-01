import csv
from collections import defaultdict

# Dateifunktionen

def get_budget_filename(month: int, year: int) -> str:
    return f"budget_{year}_{month:02d}.csv"


def load_data(filename: str) -> list[dict]:
    """CSV-Datei lesen und jede Zeile als Dict zurückgeben."""
    data = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Konvertieren der Datentypen
                row["amount"] = float(row["amount"])
                row["year"] = int(row["year"])
                row["month"] = int(row["month"])
                # Falls day in der CSV ist auch in int umwandeln
                if "day" in row and row["day"] != "":
                    row["day"] = int(row["day"])
                data.append(row)
                # Falls day existiert -> konvertieren
                if "day" in row and row["day"] != "":
                    row["day"] = int(row["day"])
    except FileNotFoundError:
        print(f"Datei {filename} nicht gefunden. Leere Liste wird zurückgegeben.")
    return data


def save_data(filename: str, data: list[dict]):
    """Liste von Dicts zurück in CSV schreiben."""
    if not data:
        print("Warnung: Keine Daten zum Speichern.")
        return
    
    with open(filename, mode="w", newline="",encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


# Auswertungsfunktionen

def show_summary(data: list[dict]):
    """Summiert Einnahmen, Ausgaben und berechnet den Saldo."""
    income = sum(entry["amount"] for entry in data if entry["amount"] > 0)
    expenses = sum(entry["amount"] for entry in data if entry["amount"] < 0)

    print("=== Zusammenfassung ===")
    print(f"Einnahmen: {income:.2f} CHF")
    print(f"Ausgaben:  {expenses:.2f} CHF")
    print(f"Saldo: {income + expenses:.2f} CHF\n")
    

def show_largest_category(data: list[dict]):
    """Findet die Kategorie mit den höchsten Gesamtausgaben."""
    category_totals = defaultdict(float)

    for entry in data:
        if entry ["amount"] < 0:
            category_totals[entry["category"]] += entry["amount"]

        if not category_totals:
            print("Keine Ausgaben vorhanden.")
            return
        
        largest = min(category_totals, key=category_totals.get)

        print("=== Kategorie mit höchsten Ausgaben ===")
        print(f"{largest}: {category_totals[largest]:.2f} CHF\n")


def show_month_entries(data: list[dict], month: int, year: int):
    """Filtert Einträge nach Monat und gibt sie tabellarisch aus."""
    filtered = [e for e in data if e["month"] == month and e["year"] == year]

    if not filtered:
        print("Keine Einträge für diesen Monat.")
        return
    
    print(f"=== Einträge für {month:02d}/{year} ===")
    print(f"{'Datum':10} {'Kategorie':15} {'Betrag':>10}")
    print("-" * 40)

    for entry in filtered:
        day = entry.get("day", 0)
        date_str = f"{day:02d}.{month:02d}.{year}"
        print(f"{date_str:10} {entry['category']:15} {entry['amount']:10.2f}")
    
    print()

# Testfunktion (Dummy-Daten)

def test_functions():
    if __name__ == "__main__":
        test_functions()
    test_data = [
        {"day": 1, "month": 5, "year": 2024, "category": "Essen",     "amount": -20.0},
        {"day": 2, "month": 5, "year": 2024, "category": "Gehalt",    "amount": 3500.0},
        {"day": 3, "month": 5, "year": 2024, "category": "Essen",     "amount": -15.0},
        {"day": 4, "month": 5, "year": 2024, "category": "Transport", "amount": -80.0},
     ]
    
    filename = get_budget_filename(5, 2024)

    save_data(filename, test_data)
    loaded = load_data(filename)

    show_summary(loaded)
    show_largest_category(loaded)
    show_month_entries(loaded, 5, 2024)

    
