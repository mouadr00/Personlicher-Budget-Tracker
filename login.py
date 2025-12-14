import hashlib
import os
import getpass

# Datei, in der das Passwort gespeichert wird (gehasht)
PASSWORD_FILE = "passwort.csv"

def hash_password(password):
    """Gibt den SHA-256-Hash des Passworts zurück."""
    return hashlib.sha256(password.encode()).hexdigest()

def save_password_hash(password):
    """Speichert den Passwort-Hash im PASSWORD_FILE."""
    with open(PASSWORD_FILE, "w") as file:
        file.write(hash_password(password))

def load_password_hash():
    """
    Lädt den Passwort-Hash aus PASSWORD_FILE.
    Gibt den Hash-String zurück oder None, falls nicht vorhanden.
    """
    if not os.path.exists(PASSWORD_FILE):
        return None
    with open(PASSWORD_FILE, "r") as file:
        return file.read().strip()

def check_password(input_password):
    """Vergleicht das eingegebene Passwort mit dem gespeicherten Hash."""
    stored_hash = load_password_hash()
    if stored_hash is None:
        return False
    return stored_hash == hash_password(input_password)

def login():
    """Führt den Login-Prozess aus und erstellt bei Bedarf ein neues Passwort"""
    if not os.path.exists(PASSWORD_FILE):
        print("Kein Passwort gefunden. Bitte neues Passwort festlegen.")
        while True:
            new_password = getpass.getpass("Neues Passwort (mind. 6 Zeichen): ")
            if len(new_password) < 6:
                print("Passwort zu kurz!")
            else:
                save_password_hash(new_password)
                print("Passwort gespeichert.")
                break
        return
    
    """Fordert den Benutzer auf, das Passwort einzugeben und prüft es."""
    # Passwort existiert -> prüfen
    # Zur Sicherheit max. 3 Versuche.
    # Benutzer wird informiert, bevor das Programm beendet wird.
    print("LOGIN - Bitte geben Sie Ihr Passwort ein.")
    for attempt in range(4):
        password = getpass.getpass("Passwort: ")
        if check_password(password):
            print("Login erfolgreich!\n")
            return True
        # Benutzer informieren, wie viele Versuche noch bleiben
        else:
            remaining = 2 - attempt
            print(f"Falsches Passwort. Noch {remaining + 1} Versuch(e).")
    print("Zu viele Fehlversuche. Programm wird beendet.")
    exit()

def change_password():
    """Ermöglicht dem Benutzer, das Passwort zu ändern."""
    current = getpass.getpass("Aktuelles Passwort: ")
    if not check_password(current):
        print("Aktuelles Passwort ist falsch.")
        return
    while True:
        new_password = getpass.getpass("Neues Passwort (mind. 6 Zeichen): ")
        if len(new_password) < 6:
            print("Passwort zu kurz!")
        else:
            save_password_hash(new_password)
            print("Passwort erfolgreich geändert!\n")
            break
