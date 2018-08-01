# coding: utf-8

import requests
import json
import sys

def Tuling(words):
    Tuling_API_KEY = "56afc3cf444447e6a56818d5b4279a08"

    body = {"key":Tuling_API_KEY,"info":words}

    url = "http://www.tuling123.com/openapi/api"
    r = requests.post(url,data=body,verify=True)

    if r:
        date = json.loads(r.text)
        print(date["text"])
        return date["text"]
    else:
        return None
