import urllib2
import json

data = { "search":[{
   "searchType":"PROXIMITY",
   "collection":"MERCHANT",
   "what": "begals",
   "where":{
   "type":"GEO",
   "value":"45.4754418,-73.5863705" }
   }]}

   

req = urllib2.Request('http://hackaton.ypcloud.io/search')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

print response.read()