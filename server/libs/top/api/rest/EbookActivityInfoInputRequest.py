'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class EbookActivityInfoInputRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.act_id = None
		self.act_name = None
		self.act_type = None
		self.condition_desc = None
		self.end_date = None
		self.seller_id = None
		self.shop_name = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.ebook.activity.info.input'
