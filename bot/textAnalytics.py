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

x = "{u'favorited': False, u'contributors': None, u'truncated': False, u'text': u'Where to buy a shirt? #TestingPython', u'is_quote_status': False, u'in_reply_to_status_id': None, u'user': {u'follow_request_sent': None, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 86791609, u'verified': False, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/697045177656025088/5c9afaXN_normal.jpg', u'profile_sidebar_fill_color': u'252429', u'profile_text_color': u'666666', u'followers_count': 197, u'profile_sidebar_border_color': u'181A1E', u'id_str': u'86791609', u'profile_background_color': u'1A1B1F', u'listed_count': 6, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif', u'utc_offset': 0, u'statuses_count': 1367, u'description': u'Driven, passionate, optimistic person, highly ambitious and always positive. I believe in setting goals for myself and achieving them.\n#MSP#KFUPM#Code#Engineer', u'friends_count': 291, u'location': u'Waterloo, Ontario', u'profile_link_color': u'2FC2EF', u'profile_image_url': u'http://pbs.twimg.com/profile_images/697045177656025088/5c9afaXN_normal.jpg', u'following': None, u'geo_enabled': True, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/86791609/1455023572', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', u'name': u'Mohannad S. Omar', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 750, u'screen_name': u'iMohannad_S', u'notifications': None, u'url': u'http://www.facebook.com/mohannad.memo', u'created_at': u'Sun Nov 01 20:08:33 +0000 2009', u'contributors_enabled': False, u'time_zone': u'London', u'protected': False, u'default_profile': False, u'is_translator': False}, u'filter_level': u'low', u'geo': None, u'id': 823068994617966593L, u'favorite_count': 0, u'lang': u'en', u'entities': {u'user_mentions': [], u'symbols': [], u'hashtags': [{u'indices': [22, 36], u'text': u'TestingPython'}], u'urls': []}, u'in_reply_to_user_id_str': None, u'retweeted': False, u'coordinates': None, u'timestamp_ms': u'1485069914856', u'source': u'<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>', u'in_reply_to_status_id_str': None, u'in_reply_to_screen_name': None, u'id_str': u'823068994617966593', u'place': {u'country_code': u'CA', u'url': u'https://api.twitter.com/1.1/geo/id/3376992a082d67c7.json', u'country': u'Canada', u'place_type': u'country', u'bounding_box': {u'type': u'Polygon', u'coordinates': [[[-141.561094, 41.676329], [-141.561094, 89.9999], [-51.053519, 89.9999], [-51.053519, 41.676329]]]}, u'full_name': u'Canada', u'attributes': {}, u'id': u'3376992a082d67c7', u'name': u'Canada'}, u'retweet_count': 0, u'created_at': u'Sun Jan 22 07:25:14 +0000 2017', u'in_reply_to_user_id': None}"
y = {
u'favorited':False,
u'contributors':None,
u'truncated':False,
u'text':u'Where to buy a shirt? #TestingPython',
u'is_quote_status':False,
u'in_reply_to_status_id':None,
u'user':{
u'follow_request_sent':None,
u'profile_use_background_image':True,
u'default_profile_image':False,
u'id':86791609,
u'verified':False,
u'profile_image_url_https':u'https://pbs.twimg.com/profile_images/697045177656025088/5c9afaXN_normal.jpg',
u'profile_sidebar_fill_color':u'252429',
u'profile_text_color':u'666666',
u'followers_count':197,
u'profile_sidebar_border_color':u'181A1E',
u'id_str':u'86791609',
u'profile_background_color':u'1A1B1F',
u'listed_count':6,
u'profile_background_image_url_https':u'https://abs.twimg.com/images/themes/theme9/bg.gif',
u'utc_offset':0,
u'statuses_count':1367,
u'description':u'Driven, passionate, optimistic person, highly ambitious and always positive. I believe in setting goals for myself and achieving them.\n#MSP#KFUPM#Code#Engineer', u'friends_count':291,
u'location':u'Waterloo, Ontario', u'profile_link_color':u'2FC2EF',
u'profile_image_url':u'http://pbs.twimg.com/profile_images/697045177656025088/5c9afaXN_normal.jpg',
u'following':None,
u'geo_enabled':True,
u'profile_banner_url':u'https://pbs.twimg.com/profile_banners/86791609/1455023572',
u'profile_background_image_url':u'http://abs.twimg.com/images/themes/theme9/bg.gif',
u'name':u'Mohannad S. Omar',
u'lang':u'en',
u'profile_background_tile':False,
u'favourites_count':750,
u'screen_name':u'iMohannad_S',
u'notifications':None,
u'url':u'http://www.facebook.com/mohannad.memo',
u'created_at':u'Sun Nov 01 20:08:33 +0000 2009',
u'contributors_enabled':False,
u'time_zone':u'London',
u'protected':False,
u'default_profile':False,
u'is_translator':False
},
u'filter_level':u'low',
u'geo':None,
u'id':823068994617966593L,
u'favorite_count':0,
u'lang':u'en',
u'entities':{
u'user_mentions':[
],
u'symbols':[
],
u'hashtags':[
{
u'indices':[
22,
36
],
u'text':u'TestingPython'
}
],
u'urls':[
]
},
u'in_reply_to_user_id_str':None,
u'retweeted':False,
u'coordinates':None,
u'timestamp_ms':u'1485069914856',
u'source':u'<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>',
u'in_reply_to_status_id_str':None,
u'in_reply_to_screen_name':None,
u'id_str':u'823068994617966593',
u'place':{
u'country_code':u'CA',
u'url':u'https://api.twitter.com/1.1/geo/id/3376992a082d67c7.json',
u'country':u'Canada',
u'place_type':u'country',
u'bounding_box':{
u'type':u'Polygon',
u'coordinates':[
[
[
-141.561094,
41.676329
],
[
-141.561094,
89.9999
],
[
-51.053519,
89.9999
],
[
-51.053519,
41.676329
]
]
]
},
u'full_name':u'Canada',
u'attributes':{
},
u'id':u'3376992a082d67c7',
u'name':u'Canada'
},
u'retweet_count':0,
u'created_at':u'Sun Jan 22 07:25:14 +0000 2017',
u'in_reply_to_user_id':None
}
coordinates1 = y[u'place'][u'bounding_box'][u'coordinates'][0][0]
coordinates2 = y[u'place'][u'bounding_box'][u'coordinates'][0][2]
print coordinates1
print coordinates2

center = ((coordinates1[0]+coordinates2[0])/2, (coordinates1[1]+coordinates2[1])/2)
print center

print json.loads(r.text)[u'documents'][0][u'keyPhrases'][0]