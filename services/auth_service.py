import hashlib
from domain.models import User
from data_access.dao import UserDao

class AuthService:
    def __init__(self):
        # UserDao initialisieren
        self.user_dao = UserDao()

    def hash_password(self, password: str) -> str:
        # Passwort mit SHA-256 hashen (vlt alten login.py übernehmen?)
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, username: str, password: str) -> bool:
        # Benutzer anhand des Benutzernamens abrufen
        user = self.user_dao.get_user_by_username(username)
        if not user:
            return False
        
        # Passwort hashen und mit dem gespeicherten Hash vergleichen
        hashed_password = self.hash_password(password)
        # Hash vergleichen mit user.password_hash aus Datenbank
        if hashed_password == user.password_hash:
        # Rückgabe True (Login erfolgreich) oder False (Login fehlgeschlagen)
            return True
        else:
            return False

    def register_user(self, username: str, password: str) -> User:
        # Überprüfen ob Benutzername bereits existiert (self.user_dao.get_user_by_username(username))
        existing_user = self.user_dao.get_user_by_username(username)
        if existing_user:
            raise ValueError("Benutzername bereits vergeben")
        # Passwort hashen
        hashed_password = self.hash_password(password)
        # Neues User-Objekt erstellen (user = User(username=..., password_hash=...))
        user = User(username=username, password_hash=hashed_password)
        # Speichern über self.user_dao.create_user(user)        
        return self.user_dao.create_user(user)
    
