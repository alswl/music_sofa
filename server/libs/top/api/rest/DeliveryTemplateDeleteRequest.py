'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class DeliveryTemplateDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.template_id = None

	def getapiname(self):
		return 'taobao.delivery.template.delete'
