from data_access.category_dao import CategoryDAO
from data_access.transaction_dao import TransactionDAO
from services.transaction_service import TransactionService
from services.budget_service import BudgetService
from services.report_service import ReportService
from ui.controllers import BudgetController


def main():
    category_dao = CategoryDAO()
    transaction_dao = TransactionDAO()

    transaction_service = TransactionService(transaction_dao, category_dao)
    budget_service = BudgetService(transaction_dao)
    report_service = ReportService(transaction_dao)

    controller = BudgetController(
        transaction_service=transaction_service,
        budget_service=budget_service,
        report_service=report_service,
    )

    user_id = 1

    controller.create_income(user_id, 3200, "Lohn", "Monatslohn", "2026-05-01")
    controller.create_expense(user_id, 120, "Lebensmittel", "Migros", "2026-05-03")
    controller.create_expense(user_id, 80, "Transport", "Zugticket", "2026-05-05")
    controller.create_expense(user_id, 200, "Freizeit", "Kino und Essen", "2026-05-10")
    controller.create_income(user_id, 400, "Nebeneinkommen", "Nebenjob", "2026-05-15")

    print("SUMMARY")
    print(controller.get_summary(user_id))

    print("\nBALANCE")
    print(controller.get_balance(user_id))

    print("\nMONTHLY REPORT")
    for transaction in controller.get_monthly_report(user_id, "2026-05"):
        print(transaction)

    print("\nMONTHLY SUMMARY")
    print(controller.get_monthly_summary(user_id, "2026-05"))

    print("\nTOP EXPENSE CATEGORY")
    print(controller.get_top_expense_category(user_id, "2026-05"))


if __name__ == "__main__":
    main()
