class BudgetService:
    """Berechnet Summen und Saldo auf Basis gespeicherter Transaktionen."""

    def __init__(self, transaction_dao) -> None:
        self.transaction_dao = transaction_dao

    def get_total_income(self, user_id: int, month: int, year: int) -> float:
        transactions = self.transaction_dao.get_transactions_by_user_and_month(user_id, month, year)
        return round(
            sum(t.amount for t in transactions if t.transaction_type == "income"),
            2,
        )

    def get_total_expenses(self, user_id: int, month: int, year: int) -> float:
        transactions = self.transaction_dao.get_transactions_by_user_and_month(user_id, month, year)
        return round(
            sum(t.amount for t in transactions if t.transaction_type == "expense"),
            2,
        )

    def calculate_balance(self, user_id: int, month: int, year: int) -> float:
        total_income = self.get_total_income(user_id, month, year)
        total_expenses = self.get_total_expenses(user_id, month, year)
        return round(total_income - total_expenses, 2)

    def get_summary(self, user_id: int, month: int, year: int) -> dict:
        total_income = self.get_total_income(user_id, month, year)
        total_expenses = self.get_total_expenses(user_id, month, year)

        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": round(total_income - total_expenses, 2),
        }
