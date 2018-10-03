#Therapy Session -- Team Bob: Jerry Ye and Ahnaf Hasan
#SoftDev1 pd7
#K14 -- Do I Know You?
#2018-10-01

from flask import Flask, render_template, session, redirect, url_for, request, flash #imports class Flask
app = Flask(__name__)#Creates an instance of Flask

app.secret_key = '\x86\xeb>/%1\xa6S\xd0\xde\xd0\nf\r\x95\x02%\xb3\x94m\x82\x03\xd4=\xb4\xf0\x87\xa36\x80\x07\xfc'
@app.route('/')#Defines index
def index():
    if 'username' in session:
        return render_template("welcome.html", user = session['username'])
    else:
        return render_template("login.html")
@app.route('/auth', methods=['POST'])
def authenticate():
    if request.form['username'] == 'Bob' and request.form['pass'] == 'isAwesome':
        session['username'] = 'Bob'
    elif request.form['username'] == 'Bob':
        flash("Incorrect password!")
        return redirect(url_for("index"))
    elif request.form['pass'] == 'isAwesome':
        flash("Incorrect Username!")
        return redirect(url_for("index"))
    else:
        flash("Incorrect password and username!")
        return redirect(url_for("index"))
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for("index"))



if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()
