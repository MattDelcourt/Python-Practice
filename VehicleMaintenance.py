'''
This program asks the user to enter the monthly costs for the following
expenses incurred from operating their automobile: loan payment, insurance, gas,
and maintenance. The program then displays the total monthly costs for these
expenses and the total annual costs for these expenses.
'''

#Declare function
def CalculateTotals(ln, ins, gas, oil, ti, main):
    #DeclareVariables
    month = 0.0
    year = 0
    #Calculate Variables
    month = ln + ins + gas + oil + ti + main
    year = month * 12
    #Print Findings
    print("Your Monthly costs are: $",format(month,".2f"),"Your yearly costs are: $",format(year,".2f"))

#Declare main
def Main():
    #Declare variables
    loanM = 0.0
    insuranceM = 0.0
    gasM = 0.0
    oilM = 0.0
    tiresM = 0.0
    maintenanceM = 0.0
    #Get inputs
    loanM = float(input("Enter loan payment:"))
    insuranceM = float(input("Enter insurance:"))
    gasM = float(input("Enter gas cost:"))
    oilM = float(input("Enter oil changes cost:"))
    tiresM = float(input("Enter tire cost:"))
    maintenanceM = float(input("Enter maintenance:"))
    #Run inputs
    CalculateTotals(loanM, insuranceM, gasM, oilM, tiresM, maintenanceM)


Main()
