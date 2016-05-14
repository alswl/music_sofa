#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright ©2014-03-28 Alex <zhirun.yu@duitang.com>
#
"""
Shop search request
"""
from top.api.base import RestApi

class ItemsSearchRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.fields = None
        self.q = None
        self.cid = None
        self.nicks = None
        self.props = None
        self.product_id = None
        self.order_by = None
        self.ww_status = None
        self.post_free = None

    def getapiname(self):
        return 'taobao.items.search'
