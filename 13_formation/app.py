from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("firstPage.html",
                            daWay = 'GET')

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    if request.method == 'GET':
        return render_template("secondPage.html",
                                user = request.args['username'],
                                method = request.method)
    else:
        return render_template("secondPage.html",
                                user = "Anon",
                                method = request.method)


if __name__ == "__main__":
    app.debug = True
    app.run()
