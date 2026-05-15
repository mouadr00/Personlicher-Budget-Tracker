from typing import List, Optional
from datetime import date
from sqlmodel import SQLModel, Field, Relationship


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

    transactions: List["Transaction"] = Relationship(back_populates="category")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    password_hash: str

    transactions: List["Transaction"] = Relationship(back_populates="user")


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    date: date
    description: Optional[str] = None
    transaction_type: str
    user_id: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")

    user: User = Relationship(back_populates="transactions")
    category: Category = Relationship(back_populates="transactions")
