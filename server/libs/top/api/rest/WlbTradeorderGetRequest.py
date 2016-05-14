'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class WlbTradeorderGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.trade_id = None
		self.trade_type = None

	def getapiname(self):
		return 'taobao.wlb.tradeorder.get'
