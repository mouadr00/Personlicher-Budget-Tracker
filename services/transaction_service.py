from datetime import datetime


class TransactionService:
    """Validiert Eingaben und erstellt Transaction-Objekte."""

    def __init__(self, transaction_dao, category_dao) -> None:
        self.transaction_dao = transaction_dao
        self.category_dao = category_dao

    def validate_amount(self, amount: float) -> float:
        try:
            amount = float(amount)
        except (TypeError, ValueError) as exc:
            raise ValueError("Betrag muss eine Zahl sein.") from exc

        if amount <= 0:
            raise ValueError("Betrag muss grösser als 0 sein.")

        return round(amount, 2)

    def validate_date(self, date_str: str) -> str:
        if not date_str or not str(date_str).strip():
            raise ValueError("Datum darf nicht leer sein.")

        try:
            parsed = datetime.strptime(str(date_str).strip(), "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError("Datum muss im Format YYYY-MM-DD sein.") from exc

        return parsed.strftime("%Y-%m-%d")

    def validate_description(self, description: str) -> str:
        return "" if description is None else str(description).strip()

    def get_category_by_name(self, category_name: str):
        if not category_name or not str(category_name).strip():
            raise ValueError("Kategorie darf nicht leer sein.")

        category = self.category_dao.get_by_name(str(category_name).strip())
        if category is None:
            raise ValueError(f"Kategorie '{category_name}' existiert nicht.")

        return category

    def add_income(self, user_id: int, amount: float, category_name: str, description: str, date_str: str):
        category = self.get_category_by_name(category_name)

        transaction = self.transaction_dao.create(
            user_id=user_id,
            transaction_type="income",
            amount=self.validate_amount(amount),
            category_id=category.id,
            description=self.validate_description(description),
            date=self.validate_date(date_str),
        )
        return transaction

    def add_expense(self, user_id: int, amount: float, category_name: str, description: str, date_str: str):
        category = self.get_category_by_name(category_name)

        transaction = self.transaction_dao.create(
            user_id=user_id,
            transaction_type="expense",
            amount=self.validate_amount(amount),
            category_id=category.id,
            description=self.validate_description(description),
            date=self.validate_date(date_str),
        )
        return transaction
