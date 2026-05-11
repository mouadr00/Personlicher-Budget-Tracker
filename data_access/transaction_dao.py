from domain.models import Transaction


class TransactionDAO:
    def __init__(self) -> None:
        self.transactions = []
        self.next_id = 1

    def create(
        self,
        user_id: int,
        transaction_type: str,
        amount: float,
        category_id: int,
        description: str,
        date: str,
        category,
    ):
        transaction = Transaction(
            id=self.next_id,
            user_id=user_id,
            transaction_type=transaction_type,
            amount=amount,
            category_id=category_id,
            description=description,
            date=date,
            category=category,
        )
        self.transactions.append(transaction)
        self.next_id += 1
        return transaction

    def get_all_by_user(self, user_id: int):
        return [t for t in self.transactions if t.user_id == user_id]
