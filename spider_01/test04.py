import urllib.request
h={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-66ecd8f7-2e5bc6d735f793c930909d5c"

}


req = urllib.request.Request("https://httpbin.org/get",headers=h)

proxies = {"http" : "127.0.0.1:7890"}
proxy_handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_handler)
# r = urllib.request.urlopen(req)
r = opener.open(req)

print(r.read().decode())


