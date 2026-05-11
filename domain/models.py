from dataclasses import dataclass


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Transaction:
    id: int
    user_id: int
    transaction_type: str
    amount: float
    category_id: int
    description: str
    date: str
    category: Category
