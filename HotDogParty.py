'''
Assume hot dogs come in packages of 10, and hotdog buns come in packages of 8. This
program calculates the number of packages of hot dogs and the number of
packages of hot dog buns needed for a cookout, with minimum amount of leftovers. The
program asks the user for the number of people attending the cookout and the
number of hot dogs each person will be given. The program then displays the following
details:
 The minimum number of packages of hot dogs required.
 The minimum number of packages of hot dog buns required
 The number of hot dogs that will be left over
 The number of hot dog buns that will be left over
'''
#Get people and hotdog info
def PartySize(people):
    #Declare Locals
    party = [0] * people
    hotDogs = 0
    dogsNeeded = 0
    totalDogs = 0
    dogPackage = 10
    dogPacks = 0
    x = 0
    for x in party:
        hotdogs = int(input("how many dogs would you like:"))
        party[x] = "Person",x,"wants:",hotdogs,"hotdogs."
        dogsNeeded += hotdogs
    while totalDogs < dogsNeeded:
        dogPacks += 1
        totalDogs += dogPackage
    print("Number of hotdog packs needed are:",dogPacks)
    return totalDogs

def CalculateBuns(dogs):
    #Declare locals
    bunPackage = 8
    bunPacks = 0
    totalBuns = 0
    while totalBuns < dogs:
        bunPacks += 1
        totalBuns += bunPackage
    print("Number of hotdog bun packages needed is: ",bunPacks,"\nTotal hotdogs need are: ",dogs,"\nTotal Buns needed are: ",totalBuns)
    

#Main
def Main():
    userAttending = int(input("Enter how many people attending: ")) 
    CalculateBuns(PartySize(userAttending))
    leave = input("")


Main()
