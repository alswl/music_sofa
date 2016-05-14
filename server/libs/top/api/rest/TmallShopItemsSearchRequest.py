'''
Created by auto_sdk on 2012-10-14 16:31:19
'''
from top.api.base import RestApi
class TmallShopItemsSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.auction_tag = None
		self.cat = None
		self.end_price = None
		self._from = None
		self.q = None
		self.sort = None
		self.start = None
		self.start_price = None
		self.user_id = None

	def getapiname(self):
		return 'tmall.shop.items.search'
