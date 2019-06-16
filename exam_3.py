import time

import requests
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345678'
app.config['MYSQL_DATABASE_DB'] = 'test_database'
app.config['MYSQL_DATABASE_HOST'] = '203.154.83.124'
app.config['MYSQL_DATABASE_POST'] = 3306

#Basic Auth
app.config['BASIC_AUTH_USERNAME'] = 'sdi'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

secure_my_api = BasicAuth(app)

mysql = MySQL()
mysql.init_app(app)


@app.route('/api/user', methods=['POST'])
def insertUser():
    data = request.get_json()
    list_user = jsonify(data)
    print list_user

    user_username = data['username']
    user_pass = data['password']
    print user_username, user_pass

    # Connect Database
    conn = mysql.connect()
    cursor = conn.cursor()
    times = time.time()

    try:
        sql = """Insert into users (username,password,create_time)values(%s,%s,%s)"""
        value = (user_username, user_pass, times)
        cursor.execute(sql, value)

    except Exception as e:
        print e
        return "failed"

    conn.commit()
    conn.close()

    sendLine(user_username)

    return "succeed"

def sendLine(user_username):
    url = 'https://notify-api.line.me/api/notify'
    token = 'ZjRnlYLyDo6WAWSu02KBAf43D4Yz1XPUHWdJTMuk8lo'
    headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}

    username = user_username
    response = requests.post(url, headers=headers, data={'message': username})

    print response.text

app.run(host="127.0.0.2")