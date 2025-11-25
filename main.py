def main():
    """
    Hauptfunktion:
    - Login ausführen
    - Budgetdaten laden
    - Hauptmenü in Schleife anzeigen
    """
  print("Willkommen beim Persönlichen Budget-Tracker!")

# Login (Passwortprüfung)
login()

# Standardmässig: aktueller Monat / Jahr
today = datetime.today()
month = today.month
year = today.year

filename = get_budget_filename(month, year)

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

def show_menu():
    """
    Zeigt das Hauptmenü an.
    """
    print("\n--- BUDGET TRACKER ---")
    print("1. Einnahme hinzufügen")
    print("2. Ausgabe hinzufügen")
    print("3. Verfügbares Budget anzeigen")
    print("4. Grösste Ausgabenkategorie anzeigen")
    print("5. Monatliche Einträge anzeigen")
    print("6. Budgetplan speichern")
    print("7. Passwort ändern")
    print("8. Programm beenden")

def handle_choice(choice, data, filename): 
    """
    Verarbeitet die Menüwahl.
    Gibt True zurück, wenn das Programm beendet werden soll.
    """
    if choice == "1":
        add_income(data)
    elif choice == "2":
        add_expense(data)
    elif choice == "3":
        show_summary(data)
    elif choice == "4":
        show_largest_category(data)
    elif choice == "5":
        
