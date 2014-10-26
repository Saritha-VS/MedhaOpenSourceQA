#! /usr/bin/python 

import urllib
import requests
import json

class PostMethodRequest():
	base_url = ""
	port = ""
	path_url = ""
	post_objectData = ""
	complete_url = ""

	def __init__(self,baseurl="",port="",pathurl=""):
		self.base_url=baseurl
		self.port = port
		self.path_url = pathurl
		print "path: ",self.pathurl," baseurl ",self.baseurl," port ",self.port
		if(self.port != ""):
			self.complete_url = self.baseurl+':'+self.port+self.pathurl
		else:
			self.complete_url = self.baseurl+self.pathurl

		if(self.requesturl != ""):
			self.complete_url = self.complete_url+'?'+self.requesturl
			self.complete_url = self.complete_url+rstrip();
		else:
			self.complete_url = self.complete_url

	def isJSONFile(filename):
		if(filename.endswith('.json')):
			print " file is JSON file "
			return true
		else:
			print " file is not a JSON file "
			return false

	def setPostDataFromFile(self,postdatafilename):
		if(isJSONFile):
			with open(postdatafilename) as data_file:    
    		post_objectData = json.load(data_file)
    	else:
    		print "Not able to set post data from given file, check the file type, it needs to be json file"

	def setPostDataFromJSON(self):

	def setAdditionalURLParameters(self):

	def getResponseCode(self):

	def makePostRequest(self):
		response = requests.post(self.complete_url,data=post_objectData)
		return response






	