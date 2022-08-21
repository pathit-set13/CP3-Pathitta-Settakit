def VATCalculate(totalPrice):
    result = totalPrice+(totalPrice*(7/100))
    return result

ExVatPrice = float(input("Enter Total Price (Exclude VAT7%): "))
print("Total Price (Include VAT7%): ", VATCalculate(ExVatPrice))