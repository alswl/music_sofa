'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class SimbaInsightCatsforecastGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.nick = None
		self.words = None

	def getapiname(self):
		return 'taobao.simba.insight.catsforecast.get'
