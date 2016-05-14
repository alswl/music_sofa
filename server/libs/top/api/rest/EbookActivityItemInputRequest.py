'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class EbookActivityItemInputRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.act_id = None
		self.item_id = None
		self.item_pic_url = None
		self.item_price = None
		self.item_title = None
		self.real_price = None

	def getapiname(self):
		return 'taobao.ebook.activity.item.input'
