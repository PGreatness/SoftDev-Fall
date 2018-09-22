# DKL_LiK-DKeriazis
# SoftDev1 pd7
# K02 -- NO-body expects the Spanish Inquisition!
# 2018-09-09

import random

# Dictionary of Soft Devos
KREWES = {
    'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed',
        'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ',
        'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen',
        'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray',
        'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li',
        'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton',
        'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil',
        'Mohammed', 'Ryan', 'Jason'],
    'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin',
        'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex',
        'Bill', 'Daniel', 'Jason'],
    'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas',
        'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin',
        'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane',
        'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']
}

def randStudent():
    # Selects random team from dictionary KREWES
    randTeam = random.choice(list(KREWES.values()))
    # Selects random name from list associated with randTeam
    randStudent = random.choice(randTeam)
    # Prints out randomly selected student
    print (randStudent)

randStudent()
