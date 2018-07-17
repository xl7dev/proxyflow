#!/usr/bin/env python
# encoding: utf-8

import datetime
from conf.settings import STORE, static_files

"""
	format http[s] flow
"""


class ProxyFlow(object):
	def __init__(self, flow):
		"""
		Acunetix-Aspect-Password:
		Cookie: acunetixCookie
		Location: acunetix_wvs_security_test
		X-Forwarded-Host: acunetix_wvs_security_test
		X-Forwarded-For: acunetix_wvs_security_test
		Host: acunetix_wvs_security_test
		Cookie: acunetix_wvs_security_test
		Cookie: acunetix
		Accept: acunetix/wvs
		Origin: acunetix_wvs_security_test
		Referer: acunetix_wvs_security_test
		Via: acunetix_wvs_security_test
		Accept-Language: acunetix_wvs_security_test
		Client-IP: acunetix_wvs_security_test
		HTTP_AUTH_PASSWD: acunetix
		User-Agent: acunetix_wvs_security_test
		Acunetix-Aspect-Queries:任意值
		Acunetix-Aspect:任意值
		"Acunetix-Aspect": "enabled",
		"Acunetix-Aspect-Password": "082119f75623eb7abd7bf357698ff66c",
		"Acunetix-Aspect-Queries": "aspectalerts",
		"""
		super(ProxyFlow, self).__init__()
		if 'Acunetix-Aspect' in flow.request.headers:
			flow.request.headers.pop('Acunetix-Aspect')
		if 'Acunetix-Aspect-Password' in flow.request.headers:
			flow.request.headers.pop('Acunetix-Aspect-Password')
		if 'Acunetix-Aspect-Queries' in flow.request.headers:
			flow.request.headers.pop('Acunetix-Aspect-Queries')
		self.flow = flow

	def parse(self):
		item = {
			"headers": self.get_request_header(),
			"method": self.get_method(),
			"scheme": self.get_scheme(),
			"port": self.get_port(),
			"path": self.get_path(),
			"url": self.get_url(),
			"extension": self.get_extension(),
			"reason": self.get_response_reason(),
			"http_version": self.get_http_version(),
			"raw": self.get_request_content(),
			"start_time": self.get_start_time(),
			"finish_time": self.get_finish_time(),
			"status_code": self.get_status_code(),
			"response_headers": self.get_response_header(),
			"content": self.get_response_content()
		}
		return item

	def get_scheme(self):
		return self.flow.request.scheme

	def get_method(self):
		return self.flow.request.method

	def get_port(self):
		return self.flow.request.port

	def get_request_header(self):
		return dict(self.flow.request.headers)

	def get_request_content(self):
		return self.flow.request.content.decode()

	def get_path(self):
		return '/{}'.format('/'.join(self.flow.request.path_components))

	def get_extension(self):
		path = self.flow.request.path_components
		if path:
			split_ext = path[-1].split('.')
			if len(split_ext) == 1:
				ext = ''
			else:
				ext = split_ext[-1]
			return ext
		else:
			ext = ''
		return ext

	def get_http_version(self):
		return self.flow.response.http_version

	def get_url(self):
		return self.flow.request.url

	def get_response_header(self):
		return dict(self.flow.response.headers)

	def get_start_time(self):
		return self.time_format(self.flow.request.timestamp_start)

	def get_finish_time(self):
		return self.time_format(self.flow.response.timestamp_end)

	def get_response_content_type(self):
		return self.flow.response.headers['Content-Type']

	def get_response_content(self):
		if STORE:
			if self.get_response_content_type() not in static_files:
				return self.flow.response.content.decode()
			else:
				return ''
		else:
			return ''

	def get_status_code(self):
		return self.flow.response.status_code

	def get_response_reason(self):
		return self.flow.response.reason

	@staticmethod
	def time_format(time):
		t = datetime.datetime.utcfromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")
		return t

	@staticmethod
	def format_header(header):
		headers = {}
		for k, v in header:
			headers[k] = v
		return headers
