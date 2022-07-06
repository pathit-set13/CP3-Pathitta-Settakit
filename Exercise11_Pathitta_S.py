number = int(input("Enter number: "))
for x in range(number):
    text = ""
    for y in range(x*2+1):
        text += "*"
    print(" "*(number-x+1), text)