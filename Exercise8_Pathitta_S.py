print("---BXG SHOP---")
print("--------------")
print("Please Login.")
UserName = input("Username: ")
PassworD = input("Password: ")
print("--------------")
if UserName == "PathitS" and PassworD == "pass1234" :
    print("Welcome, PathitS!")
    print("-------Menu-------")
    print("01 | ROASTED COFFEE BEAN 250g. (DARK)   : 670.00 THB.")
    print("02 | ROASTED COFFEE BEAN 250g. (MEDIUM) : 650.00 THB.")
    print("03 | ROASTED COFFEE BEAN 250g. (LIGHT)  : 630.00 THB.")
    print("04 | COCOA POWER 300g.                  : 240.00 THB.")
    print("05 | GREEN TEA LEAF 330g.               : 390.00 THB.")
    print("------------------")
    print("Please select the item...(01 to 05)")
    item1 = input("Item 1: ")
    if item1 == "01" :
        price1 = 670.00
    elif item1 == "02" :
        price1 = 650.00
    elif item1 == "03" :
        price1 = 630.00
    elif item1 == "04" :
        price1 = 240.00
    elif item1 == "05" :
        price1 = 390.00
    else:
        price1 = 0.00
    qty1 = int(input("Quantity (min = 1): "))
    total1 = price1*qty1
    item2 = input("Item 2: ")
    if item2 == "01" :
        price2 = 670.00
    elif item2 == "02" :
        price2 = 650.00
    elif item2 == "03" :
        price2 = 630.00
    elif item2 == "04" :
        price2 = 240.00
    elif item2 == "05" :
        price2 = 390.00
    else:
        price2 = 0.00
    qty2 = int(input("Quantity (min = 1): "))
    total2 = price2*qty2
    print("------------------")
    print("Total :",total1+total2, "THB.")
    print("------------------")
    print("-----THANK YOU----")
else:
    print("ERROR Please try again.")