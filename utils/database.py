#!/usr/bin/env python
# encoding: utf-8

import json
import redis
from conf.settings import REDISDB


class RedisDB(object):
	def __init__(self):
		self.db = redis.StrictRedis(host=REDISDB['host'], port=REDISDB['port'], password=REDISDB['password'],
									db=REDISDB['db'])

	def insert_urls(self, item):
		self.db.sadd("proxyflow", json.dumps(item))
