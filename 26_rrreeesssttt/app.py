'''
Python Flask app that uses 3 APIs: RandomCat, Cat Facts, and Climate Data
'''

import json, urllib, ast

from flask import Flask, render_template

app = Flask(__name__)

CAT_URL = "https://aws.random.cat/meow" #RandomCat API
CAT_FACT = "https://catfact.ninja/fact" #Cat Facts API

#Below is stuff for Climate Data API
CLIMATE_STUB = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country"
OPTION = '/mavg'
VAR = '/tas'
START = '/2020'
END = '/2039'
COUNTRY = '/USA'

@app.route('/')
def home():
    cat_info = urllib.request.urlopen(CAT_URL)
    cat_fact = urllib.request.urlopen(CAT_FACT)
    climate_info = urllib.request.urlopen(CLIMATE_STUB + OPTION + '/bccr_bcm2_0' + '/a2' + VAR + START + END + COUNTRY) #/bccr_bcm2_0/a2 returns a single list of values
    #print(CLIMATE_STUB + OPTION + '/bccr_bcm2_0' + '/a2' + VAR + START + END + COUNTRY)

    c_data = cat_info.read()
    catZ = cat_fact.read()
    clim_data = climate_info.read().decode() #is list, needs to be made into dict str
    clim_data = ast.literal_eval(clim_data) #ast.literal_eval(str) detects what this is a string representation of and converts it to that

    clim = clim_data[0] #take the first val of the list, the dictionary
    clim = json.dumps(clim) #turn to str to use json.loads(str) on

    catz = json.loads(catZ)
    c_loaded = json.loads(c_data)
    clim_loaded = json.loads(clim)

    months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    trueVals = {}
    for x, y in zip(months, clim_loaded['monthVals']): #aggregate the months and month data together
        trueVals[x] = y
    print(trueVals)
    return render_template('temp.html',
                            cat = c_loaded['file'],
                            start = clim_loaded['fromYear'], 
                            end = clim_loaded['toYear'],
                            months = trueVals,
                            fact = catz['fact'])

if __name__ == "__main__":
    app.debug = True
    app.run()