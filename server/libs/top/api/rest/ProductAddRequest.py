'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class ProductAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.binds = None
		self.cid = None
		self.customer_props = None
		self.desc = None
		self.extra_info = None
		self.image = None
		self.major = None
		self.market_id = None
		self.market_time = None
		self.name = None
		self.outer_id = None
		self.packing_list = None
		self.price = None
		self.property_alias = None
		self.props = None
		self.sale_props = None
		self.sell_pt = None

	def getapiname(self):
		return 'taobao.product.add'

	def getMultipartParas(self):
		return ['image']
