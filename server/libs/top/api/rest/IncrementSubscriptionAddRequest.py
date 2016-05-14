'''
Created by auto_sdk on 2012-10-14 16:31:19
'''
from top.api.base import RestApi
class IncrementSubscriptionAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.subscribe_key = None
		self.subscribe_values = None
		self.topic = None
		self.track_iids = None

	def getapiname(self):
		return 'taobao.increment.subscription.add'
