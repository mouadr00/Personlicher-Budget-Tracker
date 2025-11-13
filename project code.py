# Persönlicher Budget Tracker
#
#
#
#
#
def add_income(data):
    """Einnahme hinzufügen"""
    date = input("Datum (TT.MM.JJJJ, leer = heute): ")
    category = input("Kategorie (z.B. Lohn, Nebenjob): ")
    amount = float(input("Betrag: "))
    data.append({"Datum": date, "Typ": "Einnahme", "Kategorie": category, "Betrag": amount})
    print("Einnahme gespeichert.\n")
    
    
