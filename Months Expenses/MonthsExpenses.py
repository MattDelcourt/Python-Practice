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
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    
    plt.figure(figsize=(8, 6))
    plt.axis('equal')
    plt.title("Expenses")
    plt.pie(expenses, labels=tags, colors=colors, autopct='%1.1f%%', shadow=True)

    plt.savefig('Expenses.png')

    plt.close()

    print('<img src="Expenses.png" alt="Expenses Pie Chart">')
    
def main():
    CreatePie(CreateList())
    
main()


