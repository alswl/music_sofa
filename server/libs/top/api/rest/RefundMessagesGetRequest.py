'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class RefundMessagesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.refund_id = None

	def getapiname(self):
		return 'taobao.refund.messages.get'