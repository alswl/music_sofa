'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class JipiaoPoliciesAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.compressed_policies = None

	def getapiname(self):
		return 'taobao.jipiao.policies.add'

	def getMultipartParas(self):
		return ['compressed_policies']
