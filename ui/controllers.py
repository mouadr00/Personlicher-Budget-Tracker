class BudgetController:
    """Verbindet UI mit Services."""

    def __init__(
        self,
        transaction_service,
        budget_service,
        report_service,
    ) -> None:
        self.transaction_service = transaction_service
        self.budget_service = budget_service
        self.report_service = report_service

    def create_income(self, user_id: int, amount: float, category_name: str, description: str, date_str: str):
        return self.transaction_service.add_income(
            user_id=user_id,
            amount=amount,
            category_name=category_name,
            description=description,
            date_str=date_str,
        )

    def create_expense(self, user_id: int, amount: float, category_name: str, description: str, date_str: str):
        return self.transaction_service.add_expense(
            user_id=user_id,
            amount=amount,
            category_name=category_name,
            description=description,
            date_str=date_str,
        )

    def get_summary(self, user_id: int) -> dict:
        return self.budget_service.get_summary(user_id)

    def get_balance(self, user_id: int) -> float:
        return self.budget_service.calculate_balance(user_id)

    def get_monthly_report(self, user_id: int, month: str):
        return self.report_service.get_monthly_report(user_id, month)

    def get_monthly_summary(self, user_id: int, month: str) -> dict:
        return self.report_service.get_monthly_summary(user_id, month)

    def get_top_expense_category(self, user_id: int, month: str | None = None):
        return self.report_service.get_top_expense_category(user_id, month)
