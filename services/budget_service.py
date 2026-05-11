class BudgetService:
    """Berechnet Summen und Saldo auf Basis gespeicherter Transaktionen."""

    def __init__(self, transaction_dao) -> None:
        self.transaction_dao = transaction_dao

    def get_total_income(self, user_id: int) -> float:
        transactions = self.transaction_dao.get_all_by_user(user_id)
        return round(
            sum(t.amount for t in transactions if t.transaction_type == "income"),
            2,
        )

    def get_total_expenses(self, user_id: int) -> float:
        transactions = self.transaction_dao.get_all_by_user(user_id)
        return round(
            sum(t.amount for t in transactions if t.transaction_type == "expense"),
            2,
        )

    def calculate_balance(self, user_id: int) -> float:
        total_income = self.get_total_income(user_id)
        total_expenses = self.get_total_expenses(user_id)
        return round(total_income - total_expenses, 2)

    def get_summary(self, user_id: int) -> dict:
        total_income = self.get_total_income(user_id)
        total_expenses = self.get_total_expenses(user_id)
        balance = round(total_income - total_expenses, 2)

        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": balance,
        }
