'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class HanoiLabelListQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_name = None
		self.biz_status = None
		self.code = None
		self.current_page = None
		self.gmt_create_end = None
		self.gmt_create_start = None
		self.gmt_modified_end = None
		self.gmt_modified_start = None
		self.id = None
		self.is_total = None
		self.name = None
		self.open = None
		self.page_size = None
		self.scene = None
		self.template_id = None

	def getapiname(self):
		return 'taobao.hanoi.label.list.query'
