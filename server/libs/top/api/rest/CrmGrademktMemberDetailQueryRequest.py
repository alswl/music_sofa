'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class CrmGrademktMemberDetailQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.feather = None
		self.parameter = None

	def getapiname(self):
		return 'taobao.crm.grademkt.member.detail.query'
