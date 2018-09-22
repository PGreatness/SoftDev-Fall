from flask import Flask, render_template

app = Flask(__name__)

import csv, random



weightedOccupationList = []

occupationDic = {}



def fillList():

    #reads csv file

    csvFileObject = open( 'occupations.csv', 'r')

    dictionaryReader = csv.DictReader( csvFileObject)

    

    #looks at each row except for the last

    for row in dictionaryReader:

        if (row['Job Class'] != 'Total'):

	    

       	    #fills occupationList with occupations with frequency dependent on percentagE

            occupationDic[row['Job Class']] = row['Percentage']

            i = 0

            while i < (float(row['Percentage'])*10):

                weightedOccupationList.append(row['Job Class'])

                i+=1



#returns a randomly selected occupation from the weighted occupationList

fillList();

def randomOccupation():

    return random.choice(weightedOccupationList)





@app.route("/occupations")

def template():

    return render_template('template.html', randOcc = randomOccupation(), occList = occupationDic) 



if __name__ == "__main__":

    app.debug = True

    app.run()