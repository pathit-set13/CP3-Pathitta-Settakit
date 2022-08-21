def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Welcome!")
        return showMenu()
    else:
        print("Error!! Try again.")
        return login()


def showMenu():
    print("----- St*r Shop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelect = int(input("Select Menu (Enter 0 to Exit): "))
    return menuSelect(userSelect)


def menuSelect(userSelect):
    while userSelect != 0:
        if userSelect == 1:
            totalPrice = float(input("Enter Total Price (THB): "))
            return vatCalculator(totalPrice)
        elif userSelect == 2:
            return priceCalculator(), showMenu()
        else:
            print("Try Again")
            showMenu()
    else:
        print("Bye Bye!")
        exit()


def vatCalculator(totalPrice):
    vat = float(input("Enter VAT(%): "))
    result = print("Total Price(Include VAT): ", totalPrice * (1 + (vat / 100)), "", "THB.")
    return result, showMenu()

def priceCalculator():
    Item = int(input("Enter Quantity: "))
    totalPrice = 0
    for i in range(1, Item + 1):
        x = float(input("Price " + str(i) + ": "))
        totalPrice += x
    print("Total Price(Exclude VAT): ", totalPrice, "", "THB.")
    return vatCalculator(totalPrice), showMenu()


login()
