'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class InventoryAuthorizeSetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.authorize_type = None
		self.items = None

	def getapiname(self):
		return 'taobao.inventory.authorize.set'
