import urllib.request
# from urllib import request

# r = urllib.request.urlopen("https://movie.douban.com/top250")
r = urllib.request.urlopen("https://www.sohu.com/")
print(r.status)
print(r.msg)
print(r.read())
print(r.read().decode())