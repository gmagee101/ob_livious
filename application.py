from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    dataEntered = ""
    if 'data' in request.args:
        dataEntered = request.args.get('data')
        return dataEntered
    else:
        return "No Data"

@app.route('/home')
def home():
    return 'Different Page'
