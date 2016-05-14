'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class CrmGroupAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.group_name = None

	def getapiname(self):
		return 'taobao.crm.group.add'
