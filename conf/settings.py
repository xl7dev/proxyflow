#!/usr/bin/env python
# encoding: utf-8


# redis database connect info
REDISDB = {
	'host': '127.0.0.1',
	'port': 6379,
	'password': '',
	'db': 0
}

# store response
STORE = True

# static file filter from: http://www.iana.org/assignments/media-types/media-types.xhtml
static_files = [
	'application/x-javascript',
	'application/msword',
	'application/vnd.ms-excel',
	'application/vnd.ms-powerpoint',
	'application/x-ms-wmd',
	'application/x-shockwave-flash',
	'image/x-cmu-raster',
	'image/x-ms-bmp',
	'image/x-portable-graymap',
	'image/x-portable-bitmap',
	'image/x-icon',
	'image/jpeg',
	'image/gif',
	'image/x-xwindowdump',
	'image/png',
	'image/vnd.microsoft.icon',
	'image/x-portable-pixmap',
	'image/x-xpixmap',
	'image/ief',
	'image/x-portable-anymap',
	'image/x-rgb',
	'image/x-xbitmap',
	'image/tiff',
	'video/mpeg',
	'video/x-sgi-movie',
	'video/mp4',
	'video/x-msvideo',
	'video/quicktime'
	'audio/mpeg',
	'audio/x-wav',
	'audio/x-aiff',
	'audio/basic',
	'audio/x-pn-realaudio',
]
