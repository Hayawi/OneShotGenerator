from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route('/')
def main():
    Strengthscore = randint(3,18)
    return render_template('index.html',
        charname="Kevin",
        Strengthscore = Strengthscore,
        Strengthmod = randint(1,10))

if __name__ == '__main__':
    app.run()
