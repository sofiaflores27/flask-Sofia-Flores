import os

from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/holi')
def hello():
    return 'holis'
