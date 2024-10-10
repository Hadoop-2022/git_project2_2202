import urllib.request

r = urllib.request.urlopen("https://httpbin.org/get")

print(r.read().decode())


