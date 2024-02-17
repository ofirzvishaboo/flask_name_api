from flask import Flask, request
from db_connector import DBConnector
import requests
import os
import signal

app = Flask(__name__)
mdb_connector = DBConnector()


@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        res = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
        name = res.json()["user_name"]
        # user_name = mdb_connector.select_id(user_id)
        if name is None:
            return "<H1 id='error'>" 'no such user' + user_id + "</H1>"
        else:
            return "<H1 id='user'>" + name + "</H1>"


@app.route('/stop_server', methods=['GET'])
def stop_server():
    if request.method == 'GET':
        os.kill(os.getpid(), signal.SIGINT)
        return 'Server stopped'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)