from flask import Flask
from flask import request
app = Flask(__name__)

ValidLogins = {'a':'b', 'c':'d'}

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    dataEntered = ""
    if 'data' in request.args:
        dataEntered = request.args.get('data')
        return dataEntered
    else:
        return "No Data"

@app.route('/home/<name>')
def home(name):
    if name == "brie":
        data = request.get_json()
        if ('username' in data) and ('password' in data):
            #valid case
            if data.get('username') in ValidLogins:
                if data.get('password') == ValidLogins.get(data.get('username')):
                    #successful lookup
                    return "authenticated\n"
        return "not authenticated\n"
    elif name == "olivia":
        return "no function"
