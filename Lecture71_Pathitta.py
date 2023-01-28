menuList = []
priceList = []
def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number]," : ",priceList[number]," THB.")

def totalBill():
    print("----Total----")
    totalPrice = 0
    for i in range(len(menuList)):
        totalPrice += int(priceList[i])
    print(len(menuList)," items : ",totalPrice," THB.")

while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
totalBill()

