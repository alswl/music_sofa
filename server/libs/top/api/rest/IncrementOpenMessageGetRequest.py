'''
Created by auto_sdk on 2012-10-14 16:31:19
'''
from top.api.base import RestApi
class IncrementOpenMessageGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_modified = None
		self.page_no = None
		self.page_size = None
		self.start_modified = None
		self.subscribe_key = None
		self.subscribe_value = None
		self.topic = None
		self.track_iid = None

	def getapiname(self):
		return 'taobao.increment.open.message.get'
