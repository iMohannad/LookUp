import urllib.request
import json
from pprint import pprint

class API_request(object):

    def __init__(self, longitude, latitude, keywords):
        self.longitude = longitude
        self.latitude = latitude
        self.keywords = keywords

    def requestJSON(self):
        keywordsString = ""
        url = "http://dcr.yp.ca/api/search/popular?latitude=" + str(self.latitude) + "&longitude=" + str(self.longitude) + "&keyword="  + str(self.keywords[0])
        for i in range(1, len(self.keywords)):
            keywordsString += str("+" + str(self.keywords[i]))

        url+=str(keywordsString)
            
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return json.loads(data)

    

test = API_request(45.495, -73.578, ["polo", "shirt"])
#pprint(test.requestJSON())
pprint(test.requestJSON()["data"][0]["result"]["Merchants"])
#pprint(test.requestJSON()["data"][0]["result"]["Merchants"][0]["Translation"]["en"]["name"])
#["data"][0]["result"]["Merchants"]
#print("You are trying to buy milk, the nearest location for that is " + test.requestJSON()["data"][0]["result"]["Merchants"][0]["Translation"]["en"]["name"])
