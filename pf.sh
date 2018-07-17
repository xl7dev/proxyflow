#!/usr/bin/env bash

# start redis service
redispid=`ps aux|grep 'redis-server'|grep -v 'grep'|awk '{print $2}'`
if [ !$redispid ]; then
    redis-server > redis.log 2>&1 &
fi

# mitmproxy support http/https/socks
# mitmproxy -m regular --confdir 'ssl/' -s pf.py -p 8081 --set mode=upstream:http://127.0.0.1:8080 --set ssl_insecure=True # 上游代理设置
mitmproxy -m regular --ssl-insecure --set confdir=./ssl -s pf.py -p 8080
