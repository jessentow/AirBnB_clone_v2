#!/usr/bin/python3
"""This adds function that redirects"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """"This returns some text"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """This return other text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """This replaces text with variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """This replaces more text with another variable."""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
