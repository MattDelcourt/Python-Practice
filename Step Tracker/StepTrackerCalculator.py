'''
A Personal Fitness tracker is a wearable device that tracks one’s physical activity,
calories burned, heart rate, sleeping patterns and so on. One common physical activity
that is tracked is the number of steps that you take each day. The File named Steps.txt
contains the number of steps that a user has made each day for an entire year (Jan 1 to
Dec 31) This program reads the file, then displays the average number of steps
taken for each month and assumes the data is from a year that is not a leap year, therefore,
February has 28 days. The program then counts the number of days in the year
that the user has made 10,000 steps or more and display the number of days with
10000 or more steps and the average monthly steps.
'''

#Get infor from file to list
def FileToList():
    stepList = open("Steps.txt", "r")
    steps = 0
    total = 0
    average = 0.0
    greatDay = 0
    MONTHS = 12
    TEN_K = 10000
    for x in stepList:
        steps = x.rstrip('n')
        steps = int(steps)
        total += steps
        if steps >= TEN_K:
            greatDay += 1
    average = total / MONTHS
    print("The average mothly steps is:",format(average,".2f"),"\nYou had",greatDay,"10,000+ days great job!")
       
#Main
def Main():
    FileToList()
    leave = input("Press enter to close")


Main()
