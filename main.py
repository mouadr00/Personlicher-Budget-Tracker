import os

from datetime import datetime
from login import login, change_password
from budgetfunctions import add_income, add_expense
from data_reports import (
    get_budget_filename,
    load_data,
    save_data,
    show_summary,
    show_largest_category,
    show_month_entries,
)
from validationfunctions import input_date, load_categories

def clear_screen():
    """Bildschirm löschen (plattformunabhängig)"""
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    """Zeigt das Hauptmenü an."""
    print("\n--- BUDGET TRACKER ---\n")
    print("1. Einnahme hinzufügen")
    print("2. Ausgabe hinzufügen")
    print("3. Verfügbares Budget anzeigen")
    print("4. Grösste Ausgabenkategorie anzeigen")
    print("5. Monatliche Einträge anzeigen")
    print("6. Budgetplan speichern")
    print("7. Passwort ändern")
    print("8. Programm beenden\n")


def handle_choice(choice, data, filename): 
    """
    Verarbeitet die Menüwahl.
    Gibt True zurück, wenn das Programm beendet werden soll.
    """

    clear_screen() # Bildschirm löschen nach der Auswahl

    if choice == "1":
        add_income(data, allowed_categories)
    elif choice == "2":
        add_expense(data, allowed_categories)
    elif choice == "3":
        show_summary(data)
    elif choice == "4":
        show_largest_category(data)
    elif choice == "5": 
        try:
            # Benutzer gibt ein vollständiges Datum ein, z.B. 01.10.2025
            input_str = input("Für welches Datum (TT.MM.JJJJ)? ").strip()
            dt = datetime.strptime(input_str, "%d.%m.%Y")
            month, year = dt.month, dt.year
            # Passende Monatsdatei laden
            filename = get_budget_filename(month, year)
            month_data = load_data(filename)
            # Einträge anzeigen
            show_month_entries(month_data, month, year)
        except ValueError:
            print("Ungültiges Datumsformat. Bitte TT.MM.JJJJ verwenden.")
    elif choice == "6":
        save_data(filename, data)
        print("Budgetplan gespeichert.")
    elif choice == "7":
        change_password()
    elif choice == "8":
        # vor dem Beenden speichern
        save_data(filename, data) 
        print("Daten gespeichert. Programm wird beendet...")
        return True 
    else:
        print("Ungültige Eingabe. Bitte 1-8 wählen.")
    return False

def parse_month_year(date_str):
    """Hilfsfunktion zur Extraktion von Monat und Jahr aus Datum."""
    try:
        date = datetime.strptime(date_str, "%d.%m-%Y")
        return date.month, date.year
    except ValueError:
        print("Ungültiges Datumsformat. Bitte TT.MM.JJJJ verwenden.")
        return datetime.today().month, datetime.today().year
    

def main():

    allowed_categories = load_categories()
    
    """
    Hauptfunktion:
    - Login ausführen
    - Budgetdaten laden
    - Hauptmenü in Schleife anzeigen
    """
    print("\nWillkommen beim Persönlichen Budget-Tracker!\n")
    # Login (Passwortprüfung)
    login()

    # Standardmässig: aktueller Monat / Jahr
    today = datetime.today()
    filename = get_budget_filename(today.month, today.year)
    # Daten aus Datei laden (load_data)
    data = load_data(filename)

    # Hauptmenü-Schleife
    while True:
        show_menu()
        choice = input("Bitte Option wählen (1-8): ").strip()
        if handle_choice(choice, data, filename):
            # handle_choice gibt True zurück, wenn Programm beendet werden soll
            break

    print("Programm beendet. Auf Wiedersehen!")


# Dieser Block wird nur ausgeführt, wenn die Datei direkt gestartet wird.
# Beim Import in ein anderes Modul wird main() NICHT automatisch ausgeführt. 
if __name__ == "__main__":
    main() 
