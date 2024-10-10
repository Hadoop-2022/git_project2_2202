import urllib.request
# from urllib import request
from bs4 import BeautifulSoup
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='spider2202_douban',
                             cursorclass=pymysql.cursors.DictCursor)



#伪装头信息
h={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}


request = urllib.request.Request("https://movie.douban.com/top250",headers=h)

#打开Request对象
r = urllib.request.urlopen(request)

#读取后解码
# print(r.read().decode())


# 使用bs4解析页面
soup = BeautifulSoup(r.read().decode(), 'html.parser')
# item = soup.find_all("div",attrs={"class":"item"})
items = soup.find_all("div",class_="item")
# print(items)

with connection:
    for item in items:
        pic_div = item.find("div",class_="pic")
        img = pic_div.a.img
        name = img['alt']
        url = img['src']

        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `movie_info` (`movie_name`, `movie_url`) VALUES (%s, %s)"
            cursor.execute(sql, (name,url))

         # connection is not autocommit by default. So you must commit to save
        # your changes.
    connection.commit()

'''''''''''
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
'''''''''''