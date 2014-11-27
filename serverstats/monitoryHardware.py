#! /usr/bin/python 

import pymongo
import datetime
from pymongo import MongoClient
import json
import os

client = MongoClient('localhost', 27017)
db = client.systemStatsDB
collection = db.systemStats


def checkRAMutilization():
	usedRAM = os.popen("free -m | grep Mem | awk '{print $3}'")
	freeRAM = os.popen("free -m | grep Mem | awk '{print $4}'")
	totalRAM = os.popen("free -m | grep Mem | awk '{print $2}'")

	memused = ""
	for usage in usedRAM:
		print usage
		memused = usage
	return memused


def checkCPUutilization():
	cpuCount = os.popen("mpstat -P ALL | grep CPU | grep Linux | awk '{print $6}' | sed 's/(//'")
	cpuUsage = os.popen("mpstat -P ALL | grep -v CPU ")
	for temp in cpuUsage: 
		temp = temp.rstrip()
		usageData = temp.split("    ")
		if(len(usageData) >1):
			print temp

memused = checkRAMutilization()
checkCPUutilization()

data = {"date":datetime.datetime.utcnow(),"hardwareType":"RAM","memoryusage":memused}
collection.insert(data)
datafromDB = collection.find()

