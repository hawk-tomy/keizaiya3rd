import uuid
from datetime import datetime, timedelta


from flask import Flask, jsonify, request
import yaml


from user_manager import manager


with open('user.yaml')as f:
    userManager = manager(yaml.safe_load(f))


def usermanager_close():
    with open('user.yaml','w')as f:
        yaml.dump(userManager,f)


def checkToken(token):
    if token is  None or not token in userManager['token'].keys():
        return None
    else:
        if userManager['token', token, 'expiration_date'] < datetime.now():
            return False
        else:
            return True


def connection(func):
    def func2():
        check = checkToken(request.form.get('token'))
        if check is None:
            return jsonify({'status':'token is not found'}),400
        elif not check:
            return jsonify({'status':'token is not alive'}),418
        else:
            return func()
    return func2


app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        if name is not None:
            password = userManager['name', name,'password']
        else:
            return '',400
        if password == request.form.get('password'):
            token = str(uuid.uuid4())
            while token in userManager['token']:
                token = str(uuid.uuid4())
            userManager['name', name, 'token'] = token
            userManager['name', name, 'expiration_date'] = datetime.now()+timedelta(minutes=1)
            usermanager_close()
            return jsonify({"token": token})
        return '',418
    return '',404


@app.route('/connectionTest/',methods=['POST'])
@connection
def connectionTest():
    return jsonify({'status':'success'}),200


if __name__ == "__main__":
    app.run(debug=True)