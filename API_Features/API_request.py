import urllib.request
import json


class API_request(object):

    def __init__(self, longitude, latitude, keywords):
        self.longitude = longitude
        self.latitude = latitude
        self.keywords = keywords

    def requestJSON(self):
        keywordsString = str(self.keywords[0])
        for i in range(1, len(self.keywords)):
            keywordsString+= "+"
            keywordsString+=str(self.keywords[i])
            
        url = "http://dcr.yp.ca/api/search/popular?latitude=" + str(self.latitude) + "&longitude=" + str(self.longitude) + "&keyword=" + keywordsString
    
        data = urllib.request.urlopen(url).read().decode('utf-8')
        #print(data)
        return json.loads(data)
        #return urllib.request.urlopen(url).json()

test = API_request(45.495, -73.578, ["coffee"])
print(test.requestJSON()["timingInfo"])
