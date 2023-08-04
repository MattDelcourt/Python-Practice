#A painting company has determined that for every 112 square feet of wall space, one
#gallon of paint and eight hours of labor will be required. The company charges $25.00
#per hour for labour. This program asks the user to enter the number of square
#feet of wall space to be painted and the price of the paint per gallon. The program
#then displays the following data.
# The number of gallons of paint required
# The cost of the paint
# The hours of labour required to complete the job
# The cost of the labour to complete the job
# The total cost of the paint job.

#Calculate cost
def CalculateCost(sqFeet, paint):
    gallons = 0
    hours = 0.0
    paintCost = 0.0
    labourCost = 0.0
    total = 0.0
    SPACE = 112.00
    CPH = 25.00
    LABOUR = 8.0
    if sqFeet >= SPACE:
        gallons = int(sqFeet / SPACE)
        hours = LABOUR * gallons
        paintCost = paint * gallons
        labourCost = CPH * hours
        total = paintCost + labourCost
    print("Gallons needed:",gallons," - Total: $",format(paintCost,".2f"),"\nLabour Hours:",format(hours,".1f")," - Total: $",format(labourCost,".2f"),"\nTotal job cost: $",format(total,".2f"))

#Main
def Main():
    userFeet = 0.0
    userPaint = 0.0
    userFeet = float(input("Enter square footage of the space to be painted: "))
    userPaint = float(input("Enter the cost per gallon of paint: "))
    CalculateCost(userFeet, userPaint)

Main()
