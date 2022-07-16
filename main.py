import json
import time

from flask import *

print(__name__)
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_users():
    data = [{"id": 1, "username": "p30help", "age": 30}, {"id": 2, "username": "hello", "age": 50}]
    json_res = json.dumps(data)
    return json_res


@app.route('/user', methods=['GET'])
def get_user():
    user_id = str(request.args.get('id')) # /user/id=45454
    data = [{"id": user_id, "username": f'user-{user_id}', "age": 0}]
    json_res = json.dumps(data)
    return json_res


@app.route('/time', methods=['GET'])
def get_time():
    data = {"time": time.time()}
    json_res = json.dumps(data)
    return json_res


if __name__ == '__main__':
    app.run(port=7777)
