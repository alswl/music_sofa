'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class HanoiDocumentsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.code = None
		self.current_page = None
		self.id = None
		self.name = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.hanoi.documents.get'
