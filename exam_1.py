#-*- coding: utf8 -*-
from flask import *
import psutil as ps


app = Flask(__name__)
@app.route('/api/v1/vms/usage', methods=['GET'])
def getUtilize():
    getCPU()
    getMEM()
    getDisk()
    result = {}
    result['CPU'] = getCPU()
    result['MEM'] = getMEM()
    result['Disk'] = getDisk()
    result['Status'] = 200
    return jsonify(result)

@app.route('/api/v1/vms/usage/CPU', methods=['GET'])
def getCPU():
    return str(ps.cpu_percent(1))

@app.route('/api/v1/vms/usage/MEM', methods=['GET'])
def getMEM():
    return str(ps.virtual_memory().used/1024.0**3)

@app.route('/api/v1/vms/usage/Disk', methods=['GET'])
def getDisk():
    return str(ps.disk_usage(".").percent)


app.run(host="127.0.0.2")