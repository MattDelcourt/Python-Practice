'''
The text file named MonthsExpenses.txt that contains expenses for the last month in the following categories
 Rent (Mortgage)
 Gas
 Food
 Clothing
 Car Payment
 Miscellaneous
This Program reads the data from the file and uses matplotlib to plot a 
colour pie chart or Bar chart showing the distribution of your expenses.
to run this program you need to install matplotlib using
pip install matplotlib
'''

import matplotlib.pyplot as plt

def CreateList():
    from pyodide.http import open_url
    url = 'https://raw.githubusercontent.com/MattDelcourt/Python-Practice/master/Months%20Expenses/MonthsExpenses.txt'
    file = open_url(url)
    expenseList = []
    expenseList = file.readlines()
    x = 0
    while x < len(expenseList):
        expenseList[x].rstrip('\n')
        x += 1
        
    return expenseList

def CreatePie(expenses):
    tags = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Miscellaneous']
    plt.title("Expenses")
    plt.pie(expenses, labels=tags)

    plt.savefig('Expenses.png')

    plt.close()

    print('<img src="pie_chart.png" alt="Pie Chart">')
    
def main():
    CreatePie(CreateList())
    
main()


