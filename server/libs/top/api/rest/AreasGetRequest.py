'''
Created by auto_sdk on 2014-08-17 16:40:04
'''
from top.api.base import RestApi
class AreasGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None

	def getapiname(self):
		return 'taobao.areas.get'
