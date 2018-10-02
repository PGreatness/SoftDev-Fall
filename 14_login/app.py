import os

from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)

app.secret_key = os.urandom(32) #shhhhhh!!!!


@app.route('/')
def index():
    if 'username' in session: #check if user is already logged in
        print("true")
        return render_template("successPage.html") #they are logged in already, move them to the end page
    print("flase")
    return render_template('welcomePage.html') #new user, who dis?

@app.route('/login')
def log():
    return render_template("loginPage.html") #send them there to log in

@app.route('/register')
def register():
    return render_template("registerPage.html") #registry, WIP

@app.route('/redir')
def addToCvs():
    file = open("data/userPass.csv", "a")
    usr = request.form.get('newUser')
    passwrd = request.form.get('newPass')
    file.write(usr + "," + passwrd)
    return redirect(url_for("/login"))

@app.route('/auth', methods=['POST']) #method must be POST because sensitve data
def authenticate():
    file = open("data/userPass.csv", "r") #file reading from 03_occupation, see on GitHub
    userDict = {}
    for line in file:
        i = line.find(",")
        if i == -1: #csv file is missing, user list gone <:(
            return render_template("loginError.html",
                                    errMessage = "Internal Server Error",
                                    errCode = 500)
        usr = line[:i]
        passwrd = line[i + 1:]
        userDict[usr] = passwrd
    if userDict.get(request.form.get('username'), "None") == "None": #user is not in this csv file
        print("First triggered.")
        return render_template("loginError.html",
                                errMessage = "Unrecognized username, please try again or register below",
                                errCode = 205) #random error code makes it look legit
    if userDict.get(request.form.get('username'), "None") != request.form.get('password'): #username is there but password is wrong
        return render_template("loginError.html",
                                errMessage = "Unrecognized password, please try again",
                                errCode = 206) #random error code makes it look legit
    if userDict.get(request.form.get('username'), "None") == request.form.get('password'): #username and password match, BINGO!!!
        session['username'] = request.form.get('username') #add user to session, keeps logged in on other tabs
        print("Third triggered.")
        return render_template("successPage.html") #Success

@app.route('/end')
def endSession():
    session.pop('username', None) #remove user and say goodbye
    return redirect(url_for('index')) #send to home page

if __name__ == "__main__":
    app.debug = True
    app.run()