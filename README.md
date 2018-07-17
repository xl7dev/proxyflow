### Proxyflow

Supports HTTP/HTTPS/SOCKS5 Proxy Store to Redis

### Installation
OSX
```
brew install mitmproxy
pip3 install mitmproxy
```
### Using
*1) HTTP/HTTPS*
```
mitmproxy --ssl-insecure -m regular --set confdir=./ssl -s pf.py -p 8080
```
*2) SOCKS*
```
mitmproxy --ssl-insecure -m regular --set confdir=./ssl -s pf.py -p 8080 --mode socks5
```
*3) Upstream*
```
mitmproxy -m regular --set confdir=./ssl -s pf.py -p 8081 --set mode=upstream:http://127.0.0.1:8080 --set ssl_insecure=true
```
*4) REVERSE Proxy*
```
mitmproxy -R reverse --set confdir=./ssl -s pf.py -p 8080
```
### Data format
```
{
	"headers": {
		"Host": "httpbin.org",
		"Proxy-Connection": "keep-alive",
		"Cache-Control": "max-age=0",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:57.0) Gecko/20100101 Firefox/57.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "en-US,en;q=0.9",
		"Cookie": "_gauges_unique_year=1; _gauges_unique=1"
	},
	"method": "GET",
	"scheme": "http",
	"port": 80,
	"path": "/headers",
	"url": "http://httpbin.org/headers",
	"extension": "",
	"reason": "OK",
	"http_version": "HTTP/1.1",
	"raw": "",
	"start_time": "2018-07-17 15:47:16",
	"finish_time": "2018-07-17 15:47:17",
	"status_code": 200,
	"response_headers": {
		"Connection": "keep-alive",
		"Server": "gunicorn/19.8.1",
		"Date": "Tue, 17 Jul 2018 15:47:17 GMT",
		"Content-Type": "application/json",
		"Content-Length": "447",
		"Access-Control-Allow-Origin": "*",
		"Access-Control-Allow-Credentials": "true",
		"Via": "1.1 vegur"
	},
	"content": "{\"headers\":{\"Accept\":\"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\",\"Accept-Encoding\":\"gzip, deflate\",\"Accept-Language\":\"en-US,en;q=0.9\",\"Cache-Control\":\"max-age=0\",\"Connection\":\"close\",\"Cookie\":\"_gauges_unique_year=1; _gauges_unique=1\",\"Host\":\"httpbin.org\",\"Proxy-Connection\":\"keep-alive\",\"Upgrade-Insecure-Requests\":\"1\",\"User-Agent\":\"Mozilla/5.0 (Windows NT 10.0; rv:57.0) Gecko/20100101 Firefox/57.0\"}}\n"
}
```
