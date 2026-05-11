class ReportService:
    """Erstellt Monatsberichte und Auswertungen."""

    def __init__(self, transaction_dao) -> None:
        self.transaction_dao = transaction_dao

    def get_monthly_report(self, user_id: int, month: str):
        if not isinstance(month, str) or len(month) != 7:
            raise ValueError("Monat muss im Format YYYY-MM sein.")

        transactions = self.transaction_dao.get_all_by_user(user_id)
        return [t for t in transactions if str(t.date).startswith(month)]

    def get_top_expense_category(self, user_id: int, month: str | None = None):
        transactions = self.transaction_dao.get_all_by_user(user_id)

        if month is not None:
            if not isinstance(month, str) or len(month) != 7:
                raise ValueError("Monat muss im Format YYYY-MM sein.")
            transactions = [t for t in transactions if str(t.date).startswith(month)]

        expense_totals = {}

        for transaction in transactions:
            if transaction.transaction_type == "expense":
                category_name = transaction.category.name
                expense_totals[category_name] = expense_totals.get(category_name, 0) + transaction.amount

        if not expense_totals:
            return None

        return max(expense_totals, key=expense_totals.get)

    def get_monthly_summary(self, user_id: int, month: str) -> dict:
        monthly_transactions = self.get_monthly_report(user_id, month)

        income = round(
            sum(t.amount for t in monthly_transactions if t.transaction_type == "income"),
            2,
        )
        expenses = round(
            sum(t.amount for t in monthly_transactions if t.transaction_type == "expense"),
            2,
        )
        balance = round(income - expenses, 2)

        return {
            "month": month,
            "transactions": monthly_transactions,
            "income": income,
            "expenses": expenses,
            "balance": balance,
            "top_expense_category": self.get_top_expense_category(user_id, month),
        }
