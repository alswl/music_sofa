'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class TmallItemDescModulesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cat_id = None
		self.usr_id = None

	def getapiname(self):
		return 'tmall.item.desc.modules.get'
