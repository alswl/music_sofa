'''
Created by auto_sdk on 2012-10-14 16:31:19
'''
from top.api.base import RestApi
class IncrementSubscriptionGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None
		self.subscribe_key = None
		self.subscribe_values = None
		self.topic = None
		self.track_iids = None

	def getapiname(self):
		return 'taobao.increment.subscription.get'
