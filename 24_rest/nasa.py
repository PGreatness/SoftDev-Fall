from flask import Flask, render_template
import json, urllib

app = Flask(__name__)

@app.route('/')
def home():
    file = ""
    try:
        file = open('data/nasa.json', 'x')
        file = open('data/nasa.json', 'w')
    except FileExistsError as fe:
        print(str(fe) + '\nFile exists')
        file = open('data/nasa.json', 'w')
        
    url = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=djbElSwvBoHfV8m6Hiuzv7Or0dK8JmlOIDl1XvOW')
    info = url.read().decode()
    print("This is info:\n " + str(info))
    needed = {}
    d = json.dumps(info)
    print(d)
    file.write(d)
    needed = json.loads(info)
    print(needed)
    print("This is needed at a certain place: " + needed['url'])

    return render_template('temp.html', pic = needed['url'], para = needed['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()