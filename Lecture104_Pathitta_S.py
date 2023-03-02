class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to", self.name, self.lastName, "'s Cart")

customer1 = Customer()
customer1.name = "Pathitta"
customer1.lastName = "Settakit"
customer1.addCart()

customer2 = Customer()
customer2.name = "Sean"
customer2.lastName = "Xiao"
customer2.addCart()

customer3 = Customer()
customer3.name = "Yibo"
customer3.lastName = "Wang"
customer3.addCart()

customer4 = Customer()
customer4.name = "Exar"
customer4.lastName = "Flair"
customer4.addCart()