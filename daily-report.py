#!/usr/bin/env python
#coding=utf8

import sys
import httplib,urllib
import json

temp = "";
dHost = {}


for line in sys.stdin:
# 172.30.204.218/cpu-0/cpu-interrupt.rrd~~#MAX value=3.47464e-05#MIN value=3.47464e-05#AVERAGE value=3.47464e-05
    line = line.replace('\n','')
    strs = line.split("~~")
    dPlugin = {}
    dType={}
    dValue={}
    if len(strs)==2 :
        paths = strs[0].split("/")
        if dHost.has_key(paths[0]) :
            dPlugin=dHost[paths[0]]
        else:
            dHost[paths[0]]=dPlugin
        if dPlugin.has_key(paths[1]) :
            dType=dPlugin[paths[1]]
        else:
            dPlugin[paths[1]]=dType
        values= strs[1].split("#")
        for temp in values:
            if len(temp)>0:
                temps=temp.split(" ")
                dValue[temps[0]]=temps[1]
        dType[paths[2]]=dValue

#print dHost


httpClient = None
try:
    params = json.dumps(dHost)
    headers = {"Content-type": "application/json;charset=UTF-8"
                    , "Accept": "application/json"}

    httpClient = httplib.HTTPConnection("localhost", 8080, timeout=30)
    httpClient.request("POST", "/Monitor-web/daily/report/recive", params, headers)

    response = httpClient.getresponse()
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
