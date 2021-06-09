#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import requests,re,datetime



url = "https://yun.ythuanwei.com/es/emergency/getAbnormalEmergencyList"


headers = {
    'AuthToken': '3e47191efdc24a0099549b9865bcd78c'
}



data = {
    "employeeId": "",
    "endTime": "20210601213648",
    "eventName": "",
    "page": 1,
    "pageIndex": 1,
    "pageSize": 200,
    "projectId": "",
    "startTime": "20210601000000",
    "vehicleId": ""
}




response = requests.post(url, json=data, headers=headers)
print(response.text)

