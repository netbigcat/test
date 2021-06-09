#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import requests,re,datetime



url = "https://eat.vehicleplus.net/voss/vehicle/getVehicleStateList"


headers = {
    'Cookie': 'JSESSIONID=861D422085FD5A15652CA007D15493BA',
    'AuthToken': '045824c746c54a58aba5f3482c211948'
}



data = {
    "entId": "285B0A9F518947DF87744F23FD6B8674",
    "fields": "vehicleId,vehicleVin,vehicleLn,terminalTimeStr,dvr,pos,driverAssistant,liBattery,gpsAntenna,gpsModule,vss,tss,camera1,camera2,camera3,camera4",
    "orderBy": "",
    "orgId": "",
    "pageIndex": 1,
    "pageSize": 100,
    "serviceState": "",
    "terminalNetworkState": "",
    "vehicleLn": "",
    "vehicleSn": "",
    "vehicleVin": ""
}




response = requests.post(url, json=data, headers=headers)
print(response.text)

