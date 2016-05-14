'''
Created by auto_sdk on 2013-11-07 12:53:22
'''
from top.api.base import RestApi
class VideosSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.current_page = None
		self.fields = None
		self.keywords = None
		self.page_size = None
		self.states = None
		self.tag = None
		self.title = None
		self.uploader_id = None
		self.video_app_key = None

	def getapiname(self):
		return 'taobao.videos.search'
