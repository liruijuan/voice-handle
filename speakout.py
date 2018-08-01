# coding: utf-8

import sound2word
import urllib.request
import json
import sys


def baidu_tts_by_post(data, id, token):
    post_data = {
            "tex" : data,
            "lan" : "zh",
            "ctp" : 1,
            "cuid" : id,
            "tok" : token,
    }

    url = "http://tsn.baidu.com/text2audio"
    post_data = urllib.parse.urlencode(post_data).encode('utf-8')
    #print(post_data)
    req = urllib.request.Request(url, data = post_data)

    print("tts start request")
    resp = urllib.request.urlopen(req)
    print("tts finish request")
    resp = resp.read()
    return resp

def tts_main(words):
    token = sound2word.get_access_token()
    text = urllib.parse.quote(words)
    uuid = "11561301"
    resp = baidu_tts_by_post(text, uuid, token)

    f = open("test.mp3", "wb")
    f.write(resp)
    f.close()
    return (resp)
