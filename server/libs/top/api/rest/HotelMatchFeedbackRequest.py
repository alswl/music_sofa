'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class HotelMatchFeedbackRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.haid = None
		self.hid = None
		self.match_result = None

	def getapiname(self):
		return 'taobao.hotel.match.feedback'