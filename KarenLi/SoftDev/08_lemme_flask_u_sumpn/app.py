# Karen Li
# SoftDev1 pd7
# K08 -- Fill Yer Flask
# 2018-09-20

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def home():
    return """
    <h1> Japanese </h1>
    <h3> <a href="/hiragana">hiragana</a> </h3>
    <h3> <a href="/katakana">katakana</a> </h3>
    """

@app.route("/katakana")
def katakana():
    return """
    <img src="https://files.tofugu.com/articles/japanese/2017-07-13-katakana-chart/wikipedia-katatkana-chart.jpg" alt="katakana chart">
"""

@app.route("/hiragana")
def hiragana():
    return """
    <img src="https://files.tofugu.com/articles/japanese/2016-04-05-hiragana-chart/wikipedia-hiragana-chart.png" alt="hiragana chart"> 
    """

if __name__ == "__main__":
    app.debug = False #turn off when going live
    app.run()

