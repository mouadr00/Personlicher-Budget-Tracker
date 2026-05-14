from typing import List, Optional
from datetime import date, datetime
from sqlmodel import SQLModel, Field, Relationship

# --- Category Model ---
# Klasse erstellen die von SQLModel erbt
class Category(SQLModel, table=True):
    

# 'id' definieren als Primary Key (Optional[int], default=None, primary_key=True)
    id: Optional[int] = Field(default=None, primary_key=True)
# 'name' definieren als String (z.B. "Essen", "Miete", "Freizeit")
    name: str = Field(unique=True)

# Relationship zu den Transactions, falls eine Kategorie abrufen möchte 
    transactions: List["Transaction"] = Relationship(back_populates="category")
pass

# --- User Model ---
# Klasse erstellen die von SQLModel erbt
class User(SQLModel, table=True):

# 'id' definieren als Primary Key (Optional[int], default=None, primary_key=True)
    id: Optional[int] = Field(default=None, primary_key=True)
# 'username' definieren als String (unique=True)
    username: str = Field(unique=True)
# 'password hash' definieren als String, (SHA-256 Hash gespeichert)
    password_hash: str
# Relationship zu den Transactions defnieren
    transactions: List["Transaction"] = Relationship(back_populates="user")
pass

# --- Transaction Model ---
# Klasse erstellen die von SQLModel erbt (table=True)
class Transaction(SQLModel, table=True):

# 'id' definieren als Primary Key (Optional[int], default=None, primary_key=True)
    id: Optional[int] = Field(default=None, primary_key=True)
# 'amount' definieren als Float (z.B. 19.99)
    amount: float
# 'date' definieren als Datum (Typ datetime.date)
    date: datetime.date
# 'description' definieren als String (z.B. "Einkaufen")
    description: Optional[str] = None
# 'type' definieren als String (z.B. "einnahmen" oder "ausgaben")
    type: str
# User Fremdschlüssel definieren (user_id: int = Field(foreign_key="user.id"))
    user_id: int = Field(foreign_key="user.id")
# Category Fremdschlüssel definieren (category_id: int = Field(foreign_key="category.id"))
    category_id: int = Field(foreign_key="category.id")
# Relationship zu den Categories  und User defnieren
    user: User = Relationship(back_populates="transactions")
    category: Category = Relationship(back_populates="transactions")
pass