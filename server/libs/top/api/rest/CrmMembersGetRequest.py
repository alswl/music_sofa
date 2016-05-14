'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class CrmMembersGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.current_page = None
		self.grade = None
		self.max_last_trade_time = None
		self.max_trade_amount = None
		self.max_trade_count = None
		self.min_last_trade_time = None
		self.min_trade_amount = None
		self.min_trade_count = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.crm.members.get'
