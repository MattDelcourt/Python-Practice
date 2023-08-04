#The file named WorldSeriesWinners.txt contains the chronological list of World Series winning 
#teams from 1903 to 2019. The first line in the file is the name of the team that one in 
#1903 and the last line is the name of the team that won in 2019.
#(Note: The World series was not played in 1904 nor in 1994.) This program lets the user
#enter the name of a team (As it appears in the file), then displays the number of times that team
#has won the World Series in the time period from 1903 to 2019.The program steps through the
#list to count the number of times the selected team appears.

def CreateList(user):
    file = open("WorldSeriesWinners.txt", 'r')
    champList = []
    champList = file.readlines()
    win = 0
    x = 0
    while x < len(champList):
        if user.lower() in champList[x].lower():
            win +=1 
        x += 1

    if win > 0:
        print(win)
    else:
        print("Sorry your team didn't win any games")

def main():
    user = input("Enter a team name: ")
    user = user.lower()
    CreateList(user)

main()
