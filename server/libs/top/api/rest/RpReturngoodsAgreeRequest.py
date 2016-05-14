'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class RpReturngoodsAgreeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.address = None
		self.mobile = None
		self.name = None
		self.post = None
		self.refund_id = None
		self.remark = None
		self.tel = None

	def getapiname(self):
		return 'taobao.rp.returngoods.agree'
