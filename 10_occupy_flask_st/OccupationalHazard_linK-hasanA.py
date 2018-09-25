# OccupationalHazard: Karen Li, Ahnaf Hasan
# SoftDev1 pd07
# K #10: Jinja Tuning 
# 2018 - 09 - 24

from flask import Flask, render_template
app = Flask(__name__)
import csv, random



weightedOccupationList = []

occupationDic = {}



def fillList():

    #reads csv file

    csvFileObject = open( './data/occupations.csv', 'r')

    dictionaryReader = csv.DictReader( csvFileObject)

    

    #looks at each row except for the last

    for row in dictionaryReader:

        if (row['Job Class'] != 'Total'):

	    

       	    #fills occupationList with occupations with frequency dependent on percentage

            occupationDic[row['Job Class']] = row['Percentage']

            i = 0

            while i < (float(row['Percentage'])*10):

                weightedOccupationList.append(row['Job Class'])

                i+=1



#returns a randomly selected occupation from the weighted occupationList

fillList();

def randomOccupation():

    return random.choice(weightedOccupationList)

@app.route("/")

def home():
    return "<a href='occupations'>Click to view the occupation table</a>"



@app.route("/occupations")

def template():

    return render_template('template.html', 
                            randOcc = randomOccupation(), 
                            occDict = occupationDic,
                            title = "Occupation Data",
                            header = "United States Occupations Information",
                            info = "This page shows occupations in the United States along with the percentage of the U.S. workforce it comprises."
                            ) 



if __name__ == "__main__":

    app.debug = True

    app.run()
