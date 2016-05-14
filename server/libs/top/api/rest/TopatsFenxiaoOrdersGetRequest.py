'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class TopatsFenxiaoOrdersGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_created = None
		self.fields = None
		self.start_created = None
		self.status = None

	def getapiname(self):
		return 'taobao.topats.fenxiao.orders.get'
