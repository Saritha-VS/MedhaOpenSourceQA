from GetMethodRequest import GetRequest

getrequest = GetRequest("http://medhaws.cloudapp.net","3000","/wines")
print "response ",getrequest.make_request()

