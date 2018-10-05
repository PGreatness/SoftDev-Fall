#Team FLIPS_TABLES (Roster: Puneet Johal and Ahnaf Hasan)
#SoftDev1 pd09
#K#16: No Trouble 
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE ##done
command = "CREATE TABLE courses ( code TEXT, mark INTEGER, id INTEGER )"  #build SQL stmt, save as string
c.execute(command) #run SQL statement
with open("./raw/courses.csv") as course_file:
    reader = csv.DictReader(course_file)
    for row in reader:
        code = row['code'] #everything in the column before the first delimiter is probably called 'code'
        mark = row['mark'] #same reasoning as above
        iD = row['id'] #same reasoning as above above
        command = 'INSERT INTO courses VALUES(\"' + code + '\", \"' + mark + '\", \"' + iD + '\")' #" " are needed so put in escape chars
        c.execute(command)
        print(row['code'], row['mark'], row['id']) #just to make sure

command = "CREATE TABLE occupations ( Job Class TEXT, Percentage TEXT )"  #build SQL stmt, save as string
c.execute(command) #run SQL statement
with open("./raw/occupations.csv") as course_file:
    numberedRow = False
    reader = csv.DictReader(course_file)
    for row in reader:
        tmpRow = row['Job Class']
        percent = row['Percentage']
        command = 'INSERT INTO occupations VALUES(\"' + tmpRow + '\", \"' + percent + '\")' 
        c.execute(command)
        print(tmpRow, percent)

command = "CREATE TABLE peeps ( name TEXT, age INTEGER, id INTEGER )"  #build SQL stmt, save as string
c.execute(command) #run SQL statement
with open("./raw/peeps.csv") as course_file:
    reader = csv.DictReader(course_file)
    for row in reader:
        name = row['name']
        age = row['age']
        iD = row['id']
        command = 'INSERT INTO peeps VALUES(\"' + name + '\", \"' + age + '\", \"' + iD + '\")' 
        c.execute(command)
        print(row['name'], row['age'], row['id'])


#==========================================================

db.commit() #save changes
db.close()  #close database