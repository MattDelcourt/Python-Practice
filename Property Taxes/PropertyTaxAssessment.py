'''
A city collects property taxes based on the assessment value of a property. The 
assessment value is 60% of the property’s actual value. If a property is valued at
$100,000.00, the assessment value is $60,000.00. The property tax is calculates as
$0.75 for each $100 of assessment value. The tax for a property assessed at $60,000.00
would therefore be $450.00 This GUI program requests the user to enter the actual 
property value and then the program displays the assessed value and the property tax.
(10 marks)

'''

import taxes

def Main():
    launchTaxes = taxes.Window()

Main()
