'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class HanoiProxyValueGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_name = None
		self.data = None

	def getapiname(self):
		return 'taobao.hanoi.proxy.value.get'
