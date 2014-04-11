#!/usr/bin/env python
#coding=utf8

import sys
import httplib,urllib
import json

temp = "";
d = {}
flag = False
for line in sys.stdin:

    line = line.replace('\n','')
    if flag :
        d["info"]=line
    elif ":" in line :
        strs = line.split(":")
        d[strs[0]] =strs[1].strip()
    elif len(line)==0:
        flag=True;

print temp


httpClient = None
try:
    params = json.dumps(d)
    headers = {"Content-type": "application/json;charset=UTF-8"
                    , "Accept": "application/json"}

    httpClient = httplib.HTTPConnection("localhost", 8080, timeout=30)
    httpClient.request("POST", "/Monitor-web/alarm/add", params, headers)

    response = httpClient.getresponse()
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()