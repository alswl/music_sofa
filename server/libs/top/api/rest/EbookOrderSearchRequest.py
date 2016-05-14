'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class EbookOrderSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.page_no = None
		self.page_size = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.ebook.order.search'
