from typing import List, Optional
from datetime import date
from sqlmodel import select
from domain.models import User, Category, Transaction
from data_access.db import get_session

class UserDao:
    def get_user_by_username(self, username: str) -> Optional[User]:
# Session öffnen (get_session())
        with get_session() as session:
# Statement erstellen (select(User).where(User.username == username))
            statement = select(User).where(User.username == username)
# Statement ausführen (session.exec(statement).first())
            user = session.exec(statement).first()
# User oder None zurückgeben
            return user
        

    def create_user(self, user: User) -> User:
# Session öffnen (get_session())
        with get_session() as session:
# User in die Session hinzufügen (session.add(user))
            session.add(user)
# Änderungen speichern (session.commit())
            session.commit()
# Objekt neu laden (session.refresh(user))
            session.refresh(user)
            return user
pass

class TransactionDao:
    def add_transaction(self, transaction: Transaction) -> Transaction:
#Speichert neue Einnahem oder Ausgabe in db
# Session öffnen (get_session())
        with get_session() as session:
            session.add(transaction)
            session.commit()
            session.refresh(transaction)
            return transaction


    def get_transactions_by_user_and_month(self, user_id: int, month: int, year: int) -> List[Transaction]:
# Session öffnen (get_session())
        with get_session() as session:
# select(Transaction).where(Transaction.user_id == user_id, Transaction.date.month == month, Transaction.date.year == year)
            statement = select(Transaction).where(Transaction.user_id == user_id, Transaction.date.month == month, Transaction.date.year == year)
# Nach Datum nach Monat und Jahr filtern (Transaction.date.month == month, Transaction.date.year == year)

# Liste der Buchungen zurückgeben (session.exec(statement).all())
            transactions = session.exec(statement).all()
            return transactions
