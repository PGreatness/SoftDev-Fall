from flask import Flask

app = Flask(__name__)

@app.route('/hub')

def hello():
    print(__name__)
    return 'Hello. This is the page which is known for redirecting people.<br><br><a href="/extras">Go to Extras</a><br><a href="/rules">Go to da Rulez</a>'

@app.route('/extras')
def extras():
    print("On extras")
    return 'Only one true king can rule them all...<br><a href="/answers">Who could it be?</a><br><br><a href="/hub">Go to the Hub</a><br><a href="/rules">Go to da Rulez</a>'

@app.route('/answers')
def answer():
    print("on the answer")
    return 'HORSELESS DUDEEEEEEEEE!!!!<br>Also, the Netflix original Disenchantment is a pretty awesome show. From the makers of Simpsons.<br><br><a href="/hub">Go to the Hub</a>'
@app.route('/rules')
def rules():
    print("on Rules")
    return 'There is only one rule:<br>Be the best that you can be!<br><br><a href="/hub">Go to the Hub</a><br><a href="/extras">Go to extras</a>'
app.debug = False
app.run()
