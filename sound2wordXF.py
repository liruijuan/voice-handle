# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import json
import urllib.request

URL = "http://api.xfyun.cn/v1/service/v1/iat"
APPID = "5b574774"
API_KEY = "771cb83d1fd6a30a5bba996e4650ecb3"


def getHeader(aue, engineType):
    curTime = str(int(time.time()))
    # curTime = '1526542623'
    param = "{\"aue\":\"" + aue + "\"" + ",\"engine_type\":\"" + engineType + "\"}"
    #print("param:{}".format(param))
    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    #print("x_param:{}".format(paramBase64))

    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
    checkSum = m2.hexdigest()
   #print('checkSum:{}'.format(checkSum))
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    #print(header)
    return header


def getBody(filepath):
    binfile = open(filepath, 'rb')
    data = {'audio': base64.b64encode(binfile.read())}
    #print(data)
    #print('data:{}'.format(type(data['audio'])))
    #print("type(data['audio']):{}".format(type(data['audio'])))
    return data

def wordfromS(audioFilePath):
    aue = "raw"
    engineType = "sms8k"
   #audioFilePath = "1kXF.wav"

    print("asr start request\n")
    r = requests.post(URL, headers=getHeader(aue, engineType), data=getBody(audioFilePath))
    print("asr finish request\n")
    res = r.json()

    if not res['data'] == '':
        return res["data"]
    else:
        print(res)
        print("None")
        return None
