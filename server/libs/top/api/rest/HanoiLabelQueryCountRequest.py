'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class HanoiLabelQueryCountRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_name = None
		self.biz_status = None
		self.code = None
		self.gmt_create_end = None
		self.gmt_create_start = None
		self.gmt_modified_end = None
		self.gmt_modified_start = None
		self.id = None
		self.name = None
		self.open = None
		self.scene = None
		self.template_id = None

	def getapiname(self):
		return 'taobao.hanoi.label.query.count'
