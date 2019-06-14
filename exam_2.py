import subprocess

from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/api/ip', methods=['POST'])
def ip():
    dict = {}
    dict_value = {}
    data = request.get_json()
    print data
    print data['destination']

    for ip in data['destination']:
        # print ip
        response = subprocess.check_output(["ping ", ip])
        # print response
        # print type(response)
        r = response.split()
        dict_value[ip] = r[len(r)-1]
        # print dict_value

    dict['result'] = dict_value
    print dict
    return str(dict)

app.run(host="127.0.0.1")