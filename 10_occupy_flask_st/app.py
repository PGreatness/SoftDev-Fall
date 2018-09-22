from flask import Flask, render_template
from divine import *

app = Flask(__name__)

csvFile = open('./occupations.csv') #read csv file
diction = cvsDict(csvFile) #construct dictionary from the csv file

@app.route('/home') #home route
def goToOccupations():
    return '<h1 align = "center"><i>A Study on the Occupation of People </i>by Karen Li and Ahnaf Hasan</h1><br><a href="occupations">Click to view Occupations Table</a>'

@app.route('/occupations') #occupations route
def displayOccupations(): #renders occupation.html
                          #end product is a table and a link back to homepage
    return render_template("occupation.html",
                            title = "Occupation Breakdown", #title of page
                            header = "Occupation by Percentage", #Descriptive title
                            Discription = "Chosen Occupation:", #Label the randomly chosen occupation
                            extra = weightChoice(diction), #randomly chosen occupation
                            dictionary = diction #dictionary to iterate through and find occupations
                            ) + returnHome() #link to return to homepage

def returnHome():
    return '<a href="home">Click to go back</a>'

if __name__ == "__main__":
    app.run()