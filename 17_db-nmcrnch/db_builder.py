import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

def main():
	DB_FILE= "foo.db"
	db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
	c = db.cursor()               #facilitate db ops
	command = "CREATE TABLE {table_name}(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)".format(table_name = "peeps")
	c.execute(command)
	with open("peeps.csv", newline = "") as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	        command = 'INSERT INTO peeps VALUES ("{name}", {age}, {id}) '.format(name=row['name'],age=row['age'],id=row['id'])
	        c.execute(command)

	command = "CREATE TABLE {table_name}(code TEXT, mark INTEGER, id INTEGER)".format(table_name = "courses")
	c.execute(command)
	with open("courses.csv", newline = "") as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	        command = 'INSERT INTO courses VALUES ("{name}", {age}, {id}) '.format(name=row['code'],age=row['mark'],id=row['id'])
	        c.execute(command)
	db.commit() #save changes
	db.close()  #close database

# DB_FILE= "foo.db"
# db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
# c = db.cursor()               #facilitate db ops
# command = "CREATE TABLE {table_name}(job class TEXT, percentage INTEGER)".format(table_name = "occupations")
# c.execute(command)
# with open("occupations.csv", newline = "") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         command = 'INSERT INTO occupations VALUES ("{job}", {percentage}) '.format(job=row['Job Class'],percentage=row['Percentage'])
#         c.execute(command)
# db.commit() #save changes
# db.close()  #close database
