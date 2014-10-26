import urllib
import urllib2
import json

'''
This class is created to constrcut REST API request for GET method
and make request and return the response
'''

class GetRequest():
	pathurl = ""
	baseurl = ""
	requesturl = ""
	completeurl = ""
	port = ""

	def __init__(self,baseurl,port,path):
		self.pathurl = path
		self.baseurl = baseurl
		self.port = port
		print "path: ",self.pathurl," baseurl ",self.baseurl," port ",self.port
		if(self.port != ""):
			self.completeurl = self.baseurl+':'+self.port+self.pathurl
		else:
			self.completeurl = self.baseurl+self.pathurl

		if(self.requesturl != ""):
			self.completeurl = self.completeurl+'?'+self.requesturl
			self.completeurl = self.completeurl+rstrip();
		else:
			self.completeurl = self.completeurl

	def constructRequestURL(self):
		if(self.port != ""):
			self.completeurl = self.baseurl+':'+self.port+self.pathurl
		else:
			self.completeurl = self.baseurl+self.pathurl

		if(self.requesturl != ""):
			self.completeurl = self.completeurl+'?'+self.requesturl
			self.completeurl = self.completeurl+rstrip();
		else:
			self.completeurl = self.completeurl

	
	def set_path(self,restRequest):
		self.pathurl=restRequest

	def set_port(self,port):
		self.port = port
		
	'''
	set_baseurl: method will take the server IP address or name of the URL
	'''
	def set_baseurl(self,baseurl):
		self.baseurl = baseurl
		
	def get_url(self):
		return self.completeurl
	
	def set_urlParameters(self,parameter,vale):
		self.requesturl = self.requesturl+parameter+'='+value+'&'

	def make_request(self):
		f = urllib2.urlopen(self.completeurl)
		responsedata =  f.read()
		return responsedata
	
	def getResponseCode(self):
		print "this function will return response code"

	def getRedirectedURL(self):
		print "this function will return redirected URL "

