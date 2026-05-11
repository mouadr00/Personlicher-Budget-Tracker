from domain.models import Category


class CategoryDAO:
    def __init__(self) -> None:
        self.categories = [
            Category(id=1, name="Lohn"),
            Category(id=2, name="Nebeneinkommen"),
            Category(id=3, name="Lebensmittel"),
            Category(id=4, name="Miete"),
            Category(id=5, name="Transport"),
            Category(id=6, name="Freizeit"),
            Category(id=7, name="Sparen"),
        ]

    def get_by_name(self, name: str):
        for category in self.categories:
            if category.name.lower() == name.lower():
                return category
        return None

    def get_all(self):
        return self.categories
