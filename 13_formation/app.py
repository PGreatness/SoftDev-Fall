from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("firstPage.html")

@app.route("/auth")
def authenticate():
    return render_template("secondPage.html",
                               user = request.args['username'],
                               method = request.method)


if __name__ == __main__:
    app.debug = True
    app.run()
