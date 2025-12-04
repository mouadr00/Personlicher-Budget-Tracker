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
    print("\n--- BUDGET TRACKER ---\n")
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
        # optional andere Monate auswählen
        show_month_entries(data)
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
        print:("Ungültige Eingabe. Bitte 1-8 wählen.")
    return False


def login():
    """
    Fordert Benutzer zur Passworteingabe auf.
    - Wenn noch kein Passwort gesetzt ist: neues Passwort anlegen.
    - Sonst: Passwort 
    """
    if not os.path.exists(PASSWORD_FILE):
        print("Es wurde noch kein Passwort gesetzt.")
        new_pw = input("Bitte neues Passwort festlegen (mind. 6 Zeichen): ")
        # TODO: Validierung (Länge etc.) - Eleonora
        save_password_hash(new_pw)
        print("Passwort wurde gespeichert.")
        return

# Passwort existiert -> prüfen
# Zur Sicherheit max. 3 Versuche.
# Benutzer wird informiert, bevor das Programm beendet wird.
for attempt in range(3):
    pw = input("Bitte Passwort eingeben: ")

    if check_password(pw):
        print("Login erfolgreich.")
        return
    else:
        remaining = 2 - attempt
        print("Passwort falsch.")

        # Benutzer informieren, wie viele Versuche noch bleiben
        if remaining >= 0:
            print("Sie haben noch {remaining + 1} Versuch(e).")

    print("Zu viele Fehlversuche. Das Programm wird aus Sicherheitsgründen beendet.")
    exit(1)

def change_password():
    """
    Ermöglicht das Ändern des Passworts.
    """
    print("\n--- Passwort ändern ---")
    current = input("Aktuelles Passwort: ")
    if not check_password(current):
        print("Aktuelles Passwort ist falsch.")
        return

    new_pw = input("Neues Passwort (mind. 6 Zeichen): ")
    # TODO: Validierung der Länge - Eleonora
    save_password_hash(new_pw)
    print("Passwort wurde geändert.")


def hash_password(password):
    """
    Gibt den SHA256-Hash des Passworts zurück.
    """
    return hashlib.sha256(passwored.encode("utf-8")).hexdigest()


def save_password_hash(password):
    """ 
    Speichert den Passwort-Hash im PASSWORD_FILE.
    """
    pw_hash = hash_password(password)
    with open(PASSWORD_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["hash"])
        writer.writerow([pw_hash])


def load_password_hash():
    """
    Lädt den Passwort-Hash aus PASSWORD_FILE.
    Gibt den Hash-String zurück oder None, falls nicht vorhanden.
    """
    if not os.path.exists(PASSWORD_FILE):
        return None
    with open(PASSWORD_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows) < 2:
            return None
        return rows[1][0]


def check_password(password):
    """
    Vergleicht eingegebenes Passwort mit gespeichertem Hash.
    """
    stored_hash = load_password_hash()
    if stored_hash is None:
        return False
    return stored_hash == hash_password(password)


            
            
        
