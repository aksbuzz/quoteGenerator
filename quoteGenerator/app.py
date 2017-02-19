from flask import Flask, render_template, jsonify
from quotes import QUOTES
import random

app = Flask('__name__')


@app.route("/")
def hello():

    return render_template('index.html')


@app.route("/quote")
def generateQuote():

    return jsonify({'quote': str(randomQuote(QUOTES))})


def randomQuote(_list_):

    return random.choice(_list_)


def main():

    app.run(debug=True)


if __name__ == '__main__':

    main()
