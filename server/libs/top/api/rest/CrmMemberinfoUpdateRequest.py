'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class CrmMemberinfoUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.city = None
		self.close_trade_amount = None
		self.close_trade_count = None
		self.grade = None
		self.group_ids = None
		self.item_num = None
		self.province = None
		self.status = None
		self.trade_amount = None
		self.trade_count = None

	def getapiname(self):
		return 'taobao.crm.memberinfo.update'
