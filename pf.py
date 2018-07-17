#!/usr/bin/env python
# encoding: utf-8

from utils.format import ProxyFlow
from utils.database import RedisDB

"""
> mitmproxy -m regular --confdir 'ssl/' -s pf.py -p 8081 --set mode=upstream:http://127.0.0.1:8080 --set ssl_insecure=True # 上游代理设置
> curl -x http://127.0.0.1:8081 http://ip.cn
"""

db = RedisDB()


def response(flow):
	pf = ProxyFlow(flow)
	item = pf.parse()
	db.insert_urls(item)
