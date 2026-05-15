class ReportService:
    """Erstellt Monatsberichte und Auswertungen."""


    def __init__(self, transaction_dao) -> None:
        self.transaction_dao = transaction_dao

    def get_monthly_report(self, user_id: int, month: int, year: int):
        return self.transaction_dao.get_transactions_by_user_and_month(user_id, month, year)

    def get_top_expense_category(self, user_id: int, month: int, year: int):
        transactions = self.transaction_dao.get_transactions_by_user_and_month(user_id, month, year)

        expense_totals = {}

        for transaction in transactions:
            if transaction.transaction_type == "expense":
                category_name = transaction.category.name
                expense_totals[category_name] = expense_totals.get(category_name, 0) + transaction.amount

        if not expense_totals:
            return None

        return max(expense_totals, key=expense_totals.get)

    def get_monthly_summary(self, user_id: int, month: int, year: int) -> dict:
        monthly_transactions = self.get_monthly_report(user_id, month, year)

        income = round(
            sum(t.amount for t in monthly_transactions if t.transaction_type == "income"),
            2,
        )
        expenses = round(
            sum(t.amount for t in monthly_transactions if t.transaction_type == "expense"),
            2,
        )

        return {
            "month": f"{year}-{month:02d}",
            "transactions": monthly_transactions,
            "income": income,
            "expenses": expenses,
            "balance": round(income - expenses, 2),
            "top_expense_category": self.get_top_expense_category(user_id, month, year),
        }
