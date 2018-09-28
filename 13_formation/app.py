'''
Ahnaf Hasan
SoftDev pd07
K13 Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("firstPage.html", #render the template
                            daWay = 'GET') #choose between GET and POST

@app.route("/auth", methods=['GET', 'POST']) #courtesy of Bill Ni's thread
def authenticate():
    if request.method == 'GET': #daWay is GET
        return render_template("secondPage.html",
                                user = request.args['username'], #POST doesn't store the data in the URL
                                method = request.method) #method used, either GET or POST
    else:  #POST request used, sensitive data, shhh!
        return render_template("secondPage.html", #the page where clients are taken to
                                user = "Anon", #user value isn't stored, so has to be done manually
                                method = request.method)


if __name__ == "__main__":
    app.debug = True
    app.run()
