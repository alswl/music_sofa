'''
Created by auto_sdk on 2012-10-14 16:31:19
'''
from top.api.base import RestApi
class TmallShopsSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cat = None
		self.filter_promotion_1 = None
		self.filter_promotion_2 = None
		self.filter_promotion_3 = None
		self.filter_promotion_4 = None
		self._from = None
		self.loc = None
		self.q = None
		self.sort = None
		self.start = None
		self.style = None

	def getapiname(self):
		return 'tmall.shops.search'
