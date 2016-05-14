'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class EbookItemSendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.act_id = None
		self.act_name = None
		self.biz_order_id = None
		self.buyer_id = None
		self.ebook_lib_id = None
		self.item_id = None
		self.item_title = None
		self.out_biz_id = None
		self.seller_id = None

	def getapiname(self):
		return 'taobao.ebook.item.send'
