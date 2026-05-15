from domain.models import Transaction


class TransactionDAO:
    def __init__(self) -> None:
        self.transactions = []
        self.next_id = 1

    def add_transaction(self, transaction: Transaction) -> Transaction:
        transaction.id = self.next_id
        self.transactions.append(transaction)
        self.next_id += 1
        return transaction

    def get_all_by_user(self, user_id: int):
        return [t for t in self.transactions if t.user_id == user_id]

    def get_transactions_by_user_and_month(self, user_id: int, month: int, year: int):
        return [
            t for t in self.transactions
            if t.user_id == user_id
            and t.date.month == month
            and t.date.year == year
        ]