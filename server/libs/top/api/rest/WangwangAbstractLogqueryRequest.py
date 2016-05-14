'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class WangwangAbstractLogqueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.charset = None
		self.count = None
		self.end_date = None
		self.from_id = None
		self.next_key = None
		self.start_date = None
		self.to_id = None

	def getapiname(self):
		return 'taobao.wangwang.abstract.logquery'
