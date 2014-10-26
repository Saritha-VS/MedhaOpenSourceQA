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

	def setPostDataFromFile(self,postdatafilename):

	def setPostDataFromJSON(self):

	def setAdditionalURLParameters(self):
		
	def getResponseCode(self):

	def makePostRequest(self):
		response = requests.post(self.complete_url,data=post_objectData)
		return response






	