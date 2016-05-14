'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class FenxiaoDealerRequisitionorderRefuseRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.dealer_order_id = None
		self.reason = None
		self.reason_detail = None

	def getapiname(self):
		return 'taobao.fenxiao.dealer.requisitionorder.refuse'
