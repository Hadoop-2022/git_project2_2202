import requests
from bs4 import BeautifulSoup
import ddddocr

headers = { "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-66ecd8f7-2e5bc6d735f793c930909d5c" }
proxies = {
    "http":"http://127.0.0.1:7890",
    "https":"http://127.0.0.1:7890",
}



# 请求登录界面
s = requests.session()
login = s.get("https://www.nowapi.com/?app=account.login",headers = headers,proxies=proxies)

# 解析页面验证码
soup = BeautifulSoup(login.text,'html.parser')
image_url = soup.find_all(id = 'authCodeImg')[0]['src']

# 把验证码存储为图片
rep_code = s.get(str(image_url),headers = headers, proxies = proxies)
image_code = rep_code.content
with open('lm.jpg','wb') as f:
    f.write(image_code)
# 破译验证码
ocr = ddddocr.DdddOcr()
image = open("lm.jpg","rb").read()
result = ocr.classification(image)
print(result)

data = {
'usernm': 'charon_',
'passwd': 'jk152346',
'authcode':result,
'toUrl':'',
'app': 'accountr.aja_login'
}
r = s.post("http://www.nowapi.com/index.php?ajax=1",headers = headers,proxies = proxies,data = data)
print(r.text)

