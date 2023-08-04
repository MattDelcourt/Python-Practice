#The file pbnumbers.txt contains the winning lottery numbers selected weekly between 
#February 3, 2010 and May 11, 2016. (The file contains 654 sets of winning numbers).
#Each line in the file contains the set of six winning numbers that we selected on a given 
#date. The numbers are separated by a space and the last number in each line is the 
#complementary number for that day. For example, the first line in the file shows the 
#numbers for February 3 2010, which were 17, 22, 36, 37, 52 and the complementary 
#number is 24.
#
#This program will work with this file to search through the file and display the 10 
#most common numbers ordered by frequency. The program then displays the 10 
#least common numbers.


def CreateList():
    file = open('pbnumbers.txt', 'r')
    lottery = file.read().split()
    x = 0
    while x < len(lottery):
        lottery[x].rstrip('\n')
        lottery[x] = int(lottery[x])
        x += 1
    return lottery

def Dictionary(lottery):
    sortedDict = {}
    lotNums = {}
    for x in lottery:
        if x in lotNums:
            lotNums[x] += 1
        else:
            lotNums[x] = 1
    sortedDict = sorted(lotNums.items(), key = lambda x:x[1], reverse = True)
    for i in range(10):
        print(sortedDict[i])
    for i in range(len(sortedDict)-10,len(sortedDict)):
        print(sortedDict[i])

def RemoveNums(lottery, high, low):
    x = 0
    while x < len(lottery):
        if lottery[x] == high or lottery[x] == low:
            lottery[x].remove

def Main():
    Dictionary(CreateList())
    
Main()
