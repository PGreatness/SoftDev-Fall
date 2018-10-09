#Bob - Ahnaf Hasan and Jerry Ye
#SoftDev1 pd7
#K #17: Average, ... or Basic?
#2018-10-06

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import db_builder

db_builder.main()

def selectStudents():
    command = "SELECT name,id FROM peeps"
    cur = c.execute(command)
    return cur.fetchall()
def getAvg(studentID):
    command = "SELECT mark FROM courses WHERE courses.id = {id}".format(id = studentID)
    cur = c.execute(command)
    marks = cur.fetchall()
    numClasses = 0
    total = 0
    for grade in marks:
        total += grade[0]
        numClasses += 1
    return total / numClasses
def genTable(studentAvgs):
    command = "CREATE TABLE {table_name}(name TEXT, id INTEGER PRIMARY KEY, average INTEGER)".format(table_name = "peeps_avg")
    c.execute(command)
    for student in studentAvgs:
        com = 'INSERT INTO peeps_avg VALUES ("{name}", {id}, {grade}) '.format(name=student[0],id=student[1],grade=student[2])
        c.execute(com)
DB_FILE= "foo.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()
def main():
    Students = selectStudents()
    StudentAvgs = []
    for student in Students:
        list = []
        list.append(student[0])
        list.append(student[1])
        list.append(getAvg(student[1]))
        StudentAvgs.append(list)
    for student in StudentAvgs:
        print(student[0],student[1],student[2])
    genTable(StudentAvgs)
def add_courses(code, mark, id):
    command = 'INSERT INTO courses VALUES("{}", {}, {})'.format(code, str(mark), str(id))
    c.execute(command)
add_courses('AI', 65, 1)
add_courses('calc', 99, 1)
main()
db.commit()
db.close()
