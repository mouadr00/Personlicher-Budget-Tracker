import hashlib
import os
import getpass

PASSWORD_FILE = "passwort.csv"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(input_password):
    if not os.path.exists(PASSWORD_FILE):
        return False
    with open(PASSWORD_FILE, 'r') as file;
        stored_hash = file.read().strip()
    return stored_hash == hash_password(input_password)

def login():
    print("Willkommen! Bitte geben Sie Ihr Passwort ein.")
    for attempt in range(3):
        password = getpass.getpass("Passwort: ")
        if check_password(password):
            print("Login erfolgreich!\n")
            return True
        else:
            print("Falsches Passwort. Versuchen Sie es erneut.")
    print("Zu viele Fehlversuche. Programm wird beendet.")
    exit()

def change_password():
    print("\n Passwort ändern:")
    while True:
        new_password = getpass.getpass("Neues Passwort (mind. 6 Zeichen): ")
        if len(new_password) < 6:
            print("Passwort zu kurz!")
        else:
            with open(PASSWORD_FILE, 'w') as file:
                file.write(hash_password(new_password))
            print("Passwort erfolgreich geändert!\n")
            break
  
