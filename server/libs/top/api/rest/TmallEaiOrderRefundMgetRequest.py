'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class TmallEaiOrderRefundMgetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.start_time = None
		self.status = None
		self.use_has_next = None

	def getapiname(self):
		return 'tmall.eai.order.refund.mget'
