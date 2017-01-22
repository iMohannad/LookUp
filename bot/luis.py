
from luis_sdk import LUISClient
import json


class Luis(object):
	"""docstring for Luis"""
	def __init__(self, APPID, APPKEY):
		super(Luis, self).__init__()
		self.APPID = APPID
		self.APPKEY = APPKEY

	def sendArg(self, TEXT):
		CLIENT = LUISClient(self.APPID, self.APPKEY, True)
		res = CLIENT.predict(TEXT)
		return res

	def process_res(self, res):
		'''
		A function that processes the luis_response object and prints info from it.
		:param res: A LUISResponse object containing the response data.
		:return: None
		'''
		#print(u'---------------------------------------------')
		#print(u'LUIS Response: ')
		#print(u'Query: ' + res.get_query())
		print(u'Top Scoring Intent: ' + res.get_top_intent().get_name())
		"""if res.get_dialog() is not None:
		if res.get_dialog().get_prompt() is None:
		print(u'Dialog Prompt: None')
		else:
		print(u'Dialog Prompt: ' + res.get_dialog().get_prompt())
		if res.get_dialog().get_parameter_name() is None:
		print(u'Dialog Parameter: None')
		else:
		print('Dialog Parameter Name: ' + res.get_dialog().get_parameter_name())
		print(u'Dialog Status: ' + res.get_dialog().get_status())"""
		print(u'Entities:')
		for entity in res.get_entities():
			print(u'"%s":' % entity.get_name())
			print(u'Type: %s, Score: %s' % (entity.get_type(), entity.get_score()))
    	