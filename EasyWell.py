#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import requests
import serial
from time import sleep

port = "/dev/ttyUSB0"
ser = serial.Serial(port, 19200, timeout=0)

while True:

    data = ser.read(9999)
    if len(data) > 0:
	    reOut = re.search("(?<=Zone )(.+? .+?)\s+Z=([0-9\.]+)\s+T=([0-9\.]+)", data)

	    if reOut:
	        if reOut.group(1) == "Temperature Distribution":
	            r = requests.get("http://192.168.12.55/Api/EasyIoT/Control/Module/Virtual/N" + str(int(reOut.group(2)) + 1) + "S0/ControlLevel/" + reOut.group(3),auth=('admin', 'admin'))
	        else:
	            r = requests.get("http://192.168.12.55/Api/EasyIoT/Control/Module/Virtual/N" + str(int(reOut.group(2)) + 11) + "S0/ControlLevel/" + reOut.group(3),auth=('admin', 'admin'))
	    
    sleep(0.5)

ser.close()





    

    

