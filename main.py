# Ein einfaches Konsolen-Kassenprogramm in Python ohne Verwendung von Bibliotheken

# Ein Wörterbuch, um die Speisekartenartikel und ihre Preise zu speichern
menu = {
    "Heißgetränke": {
        "Kaffee": 3000,
        "Tee": 2000,
        "Heiße Schokolade": 4000,
        "Cappuccino": 5000
    },
    "Kuchen": {
        "Schokoladenkuchen": 8000,
        "Vanillekuchen": 7000,
        "Heidelbeerkuchen": 9000,
        "Orangenkuchen": 7500
    }
}

# Ein Wörterbuch, um die Bestellungen für jeden Tisch zu speichern
orders = {}

# Sprachvariable
current_language = "Deutsch"


# Funktion zum Anzeigen der Speisekartenartikel und ihrer Preise
def display_menu():
    print(f"Liste und Preise der Produkte ({current_language}):")
    category_number = 1
    for category, items in menu.items():
        print(f"{category_number}. {category}:")
        item_number = 1
        for item, price in items.items():
            print(f"   {item_number}. {item}: {price} Toman")
            item_number += 1
        category_number += 1
        print()


# Funktion zum Entgegennehmen einer Bestellung von einem Kunden
def take_order():
    table = input("Geben Sie Ihre Tischnummer ein: ")
    if table not in orders:
        orders[table] = []
    while True:
        display_menu()
        category_number = input(
            "Geben Sie die Nummer Ihrer gewünschten Kategorie ein (Lassen Sie es leer, um die Bestellung abzuschließen): ")
        if category_number == "":
            break
        category_number = int(category_number)
        if 1 <= category_number <= len(menu):
            category = list(menu.keys())[category_number - 1]
            item_number = input(
                "Geben Sie die Nummer Ihres gewünschten Produkts ein (Lassen Sie es leer, um eine andere Kategorie auszuwählen): ")
            if item_number == "":
                continue
            item_number = int(item_number)
            if 1 <= item_number <= len(menu[category]):
                item = list(menu[category].keys())[item_number - 1]
                orders[table].append((category, item))
                print(f"Ihr Produkt '{item}' wurde Ihrer Bestellung hinzugefügt!")
            else:
                print("Die angegebene Nummer entspricht keinem Produkt in der Liste!")
        else:
            print("Die angegebene Nummer entspricht keiner Kategorie in der Liste!")

    print(f"Ihre Bestellung wurde erfolgreich aufgenommen! Ihre Tischnummer ist {table}.")


# Funktion zum Berechnen der Rechnung für einen Kunden
def calculate_bill():
    table = input("Geben Sie Ihre Tischnummer ein: ")
    if table in orders:
        bill = 0
        print("Ihre Bestellung umfasst folgende Artikel:")
        for category, item in orders[table]:
            price = menu[category][item]
            bill += price
            print(f"{item}: {price} Toman")
        print(f"Ihr Gesamtbetrag beträgt: {bill} Toman")
    else:
        print("Ihre Tischnummer ist im System nicht registriert!")


# Funktion zum Anzeigen der Optionen für den Kunden
def display_options():
    print("Bitte wählen Sie eine Option:")
    print("1. Produkt bestellen")
    print("2. Rechnung anzeigen")
    print("3. Sprache ändern")
    print("4. Programm verlassen")


# Funktion zur Auswahl der Sprache
def select_language():
    global current_language
    print("Bitte wählen Sie Ihre Sprache:")
    print("1. Deutsch")
    print("2. Persisch")
    option = input("Geben Sie Ihre Option ein: ")
    if option == "1":
        current_language = "Deutsch"
        print("Die Sprache wurde auf Deutsch geändert.")
    elif option == "2":
        current_language = "Persisch"
        print("Die Sprache wurde auf Persisch geändert.")
    else:
        print("Ungültige Option! Die Sprache bleibt unverändert.")


# Hauptschleife zum Ausführen der Anwendung
while True:
    display_options()
    option = input("Geben Sie Ihre Option ein: ")
    if option == "1":
        take_order()
    elif option == "2":
        calculate_bill()
    elif option == "3":
        select_language()
    elif option == "4":
        print("Vielen Dank für die Nutzung der Anwendung!")
        break
    else:
        print("Ungültige Option!")

    # Automatisches Zurückkehren zur Hauptschleife nach Abschluss einer Bestellung
    print("Zurück zur Hauptoption...")
# Hauptschleife zum Ausführen der Anwendung
while True:
    display_options()
    option = input("Geben Sie Ihre Option ein: ")
    if option == "1":
        take_order()
    elif option == "2":
        calculate_bill()
    elif option == "3":
        select_language()
    elif option == "4":
        print("Vielen Dank für die Nutzung der Anwendung!")
        break
    else:
        print("Ungültige Option!")

    # Automatisches Zurückkehren zur Hauptschleife nach Abschluss einer Bestellung
    print("Zurück zur Hauptoption...")
    # Hauptschleife zum Ausführen der Anwendung
    while True:
        display_options()
        option = input("Geben Sie Ihre Option ein: ")
        if option == "1":
            take_order()
            # Automatisches Zurückkehren zur Hauptschleife nach Abschluss einer Bestellung
            print("Zurück zur Hauptoption...")
        elif option == "2":
            calculate_bill()
            # Automatisches Zurückkehren zur Hauptschleife nach Abschluss einer Bestellung
            print("Zurück zur Hauptoption...")
        elif option == "3":
            select_language()
            # Automatisches Zurückkehren zur Hauptschleife nach Abschluss einer Bestellung
            print("Zurück zur Hauptoption...")
        elif option == "4":
            print("Vielen Dank für die Nutzung der Anwendung!")
            break
        else:
            print("Ungültige Option!")
