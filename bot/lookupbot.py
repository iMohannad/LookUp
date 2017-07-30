import os
from markovbot import MarkovBot
import urllib2
import json

# Initalize a MarkovBot instance
lookupbot = MarkovBot()

# Before any text can be generated, the MarkovBot needs to read something. 
dirname = os.path.dirname(os.path.abspath(__file__))
#Construct the path to the book
book = os.path.join(dirname, u'Freud_Dream_Psychology.txt')
#make the bot read the book
lookupbot.read(book)

print dirname

first_text = lookupbot.generate_text(25, seedword=['dream', 'psychoanalysis'])
print("lookupbot says: ")
print(first_text)


# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = ''
# Consumer Secret (API Secret)
cons_secret = ''
# Access Token
access_token = ''
# Access Token Secret
access_token_secret = ''

#Login to twitter
lookupbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)


###  The bot can do 2 things:
###	 1. Generate tweets periodically
###  2. Reply to a certain target string, 
###     which the bot will use to track what happens on twitter
	
targetstring = "#askYPP"
keywords = ['buy', 'purchase', 'find']
prefix = None
suffix = None
maxconvdepth = None

# Start auto-responding to tweets
lookupbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix
	, suffix=suffix, maxconvdepth=maxconvdepth)

count = 0
while (count < 100):
	count = count


