#Get user to choose their province
Province = { "BC": 0.12, "AB": 0.05, "SK": 0.11, "MB": 0.12, "ON": 0.13, "QC": 0.14975, "NL": 0.15, "NB": 0.15, "NS": 0.15, "PE": 0.15}
tax = Province.get(input("Enter your province abbreviation: "))
print(tax)

#Get user input for items.
items = {}

while len(items) < 5:
    itemName = input("Enter item name or x to stop entering items: ")
    if itemName == "x":
        break
        
    items[itemName] = float(input("Enter item price: "))
    
    

#Calculate the sub total, tax, and total after tax.
subTotal = 0.0
for a, b in items.items():
    print(a, ": ", b)
    subTotal += b
salesTax = float(subTotal * tax)
total = float(subTotal + salesTax)

#Display the totals and tax rounded to the nearest 2 decimal places.
print("Your subtotal is: ", format(subTotal, ",.2f"), "\nthe tax is: ", format(salesTax, ",.2f"), "\nthe total sale with tax = ", format(total, ",.2f"))

#just to keep terminal open
xit = input("Enter anything to exit: ")
