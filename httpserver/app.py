import uuid
from datetime import datetime, timedelta

from flask import Flask, jsonify, request
import yaml


with open('user.yaml')as f:
    userdict = yaml.safe_load(f)

def userdict_close():
    with open('user.yaml','w')as f:
        yaml.dump(userdict,f)

def checkToken(token):
    if token is  None or not token in userdict['tokens'].keys():
        return None
    else:
        user = userdict['tokens'][token]
        if userdict['users'][user]['token'][1] < datetime.now():
            return False
        else:
            return True

def connection(func):
    def func2():
        check = checkToken(request.form.get('token'))
        if check is None:
            return jsonify({'status':'token is not found'}),400
        elif not check:
            return jsonify({'status':'token is not alived'}),418
        else:
            return func()
    return func2

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        if name is not None:
            password = userdict['users'].get(name).get('password')
        else:
            return '',400
        if password == request.form.get('password'):
            if (usertoken := userdict['users'][name])['token'] != []:
                temp = usertoken['token'][0]
                usertoken['token'] = []
                userdict['tokens'].pop(temp)
            token = str(uuid.uuid4())
            while token in userdict['tokens']:
                token = str(uuid.uuid4())
            userdict['users'][name]['token'] = [token,datetime.now()+timedelta(minutes=1)]
            userdict['tokens'][token] = name
            userdict_close()
            return jsonify({"token": token})
        return '',418
    return '',404

@app.route('/connectionTest/',methods=['POST'])
@connection
def connectionTest():
    return jsonify({'status':'success'}),200

if __name__ == "__main__":
    app.run(debug=True)