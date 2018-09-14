#Team randomlyMerged (Roster: Ahnaf Hasan and Puneet Johal)
#SoftDev1 pd7
#K02 -- NO-body expects the Spanish Inquisition!
#2018-09-07


KREWES = {

        'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],

        'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],

        'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']
}

#import "random" library in order to use its functions
import random

#picks a random team
def teamPicker():
    #pick a random int from 1 to 3 inclusive
    x = random.randint(1,3)
    if x == 1:
        return "w"
    elif x == 2:
        return "m"
    else:
        return "x"

def randomizer():
    #var team will have the same value as the key returned by function teamPicker
    #var team is a list
    teamstr = teamPicker()
    team = KREWES[teamstr]
    #pick a random int in range 0 to the final index of list team
    y = random.randint(0,len(team)-1)
    #print the value (name) at the random index
    print( team[y] + ", from krew " + teamstr)
