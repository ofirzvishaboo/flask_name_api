from flask import Flask, request
from db_connector import DBConnector
import os
import signal

app = Flask(__name__)
mdb_connector = DBConnector()


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        mdb_connector.add_user(user_id, user_name)
        return {'status': 'ok', 'user name': user_name}, 200  # status code
    elif request.method == 'GET':
        user_name = mdb_connector.select_id(user_id)
        return {'status': 'ok', 'user_name': user_name}, 200
    elif request.method == 'PUT':
        request_data = request.json
        new_name = request_data.get('user_name')
        mdb_connector.put_user(user_id, new_name)
        return {'status': 'ok', 'new username': new_name}, 200
    elif request.method == 'DELETE':
        mdb_connector.delete_user(user_id)
        return {'Deleted user_id': user_id}, 200


@app.route('/stop_server', methods=['GET'])
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'


if __name__ == '__main__':
    # need to change host for other jenkinsfile-1
    app.run(host='0.0.0.0', port=3000)
