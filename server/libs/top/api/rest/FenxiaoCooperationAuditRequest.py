'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class FenxiaoCooperationAuditRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.audit_result = None
		self.product_line_list_agent = None
		self.product_line_list_dealer = None
		self.remark = None
		self.requisition_id = None

	def getapiname(self):
		return 'taobao.fenxiao.cooperation.audit'
