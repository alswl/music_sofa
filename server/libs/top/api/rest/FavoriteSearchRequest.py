'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class FavoriteSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.collect_type = None
		self.page_no = None

	def getapiname(self):
		return 'taobao.favorite.search'
