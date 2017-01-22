import requests, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'e4756db13169403c9244e90c001e4833',
}

params = {
    
}

body = {
  "documents": [
    {
      "language": "en",
      "id": "string",
      "text": "WHERE CAN I BUY A SHIRT"
    }
  ]
}
url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases'
r = requests.post(url, data=json.dumps(body), headers=headers)

print json.loads(r.text)[u'documents'][0][u'keyPhrases'][0]