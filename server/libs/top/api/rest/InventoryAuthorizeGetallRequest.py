'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class InventoryAuthorizeGetallRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.sc_item_id_list = None
		self.store_code_list = None

	def getapiname(self):
		return 'taobao.inventory.authorize.getall'
