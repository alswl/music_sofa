'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class TraderateListAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.anony = None
		self.content = None
		self.result = None
		self.role = None
		self.tid = None

	def getapiname(self):
		return 'taobao.traderate.list.add'
