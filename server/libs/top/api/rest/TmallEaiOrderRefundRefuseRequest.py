'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class TmallEaiOrderRefundRefuseRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.refund_id = None
		self.refund_phase = None
		self.refund_version = None
		self.refuse_message = None
		self.refuse_proof = None

	def getapiname(self):
		return 'tmall.eai.order.refund.refuse'

	def getMultipartParas(self):
		return ['refuse_proof']
