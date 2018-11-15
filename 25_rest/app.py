import json, urllib

from flask import Flask, render_template

app = Flask(__name__)

BASE_URL = "http://apilayer.net/api/live?access_key="
API_KEY = "13a9f45bcebac803ec84495f8d02c9b5"
CURRENCIES = "USD,AUD,CAD,PLN,MXN,BDT"
FORMAT = '1'

@app.route('/')
def home():
    URL = BASE_URL + API_KEY + "&currencies=" + CURRENCIES + "&format=" + FORMAT
    print(URL)
    data = urllib.request.urlopen(URL)
    dictionary = json.loads(data.read())
    check = json.dumps(dictionary)
    print(check)
    return render_template('temp.html', success = dictionary['success'], source = dictionary['source'], data = dictionary['quotes'])

if __name__ == "__main__":
    app.debug = True
    app.run()