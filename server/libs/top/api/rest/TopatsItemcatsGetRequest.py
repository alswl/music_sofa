'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class TopatsItemcatsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cids = None
		self.output_format = None
		self.type = None

	def getapiname(self):
		return 'taobao.topats.itemcats.get'
