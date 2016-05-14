'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class AlipayUserGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.auth_token = None
		self.fields = None

	def getapiname(self):
		return 'alipay.user.get'
