'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class CaipiaoOrdercreatePresentorderRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.dlt_pursue = None
		self.fees = None
		self.issue = None
		self.lottery_type_id = None
		self.mobiles = None
		self.multis = None
		self.numbers = None
		self.reward_id = None
		self.shop_id = None
		self.stakes = None
		self.total_fee = None
		self.ttid = None
		self.words = None

	def getapiname(self):
		return 'taobao.caipiao.ordercreate.presentorder'
