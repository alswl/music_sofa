'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class FenxiaoDealerRequisitionorderRemarkUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.dealer_order_id = None
		self.supplier_memo = None
		self.supplier_memo_flag = None

	def getapiname(self):
		return 'taobao.fenxiao.dealer.requisitionorder.remark.update'
