menuList = []
def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(number+1,".",menuList[number][0],"---",menuList[number][1]," THB.")

def totalBill():
    print("----Total----")
    totalPrice = 0
    for i in range(len(menuList)):
        totalPrice += int(menuList[i][1])
    print(len(menuList)," items : ",totalPrice," THB.")

while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])

showBill()
totalBill()
