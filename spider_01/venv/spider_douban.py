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


request = urllib.request.Request("https://movie.douban.com/top250?start=0&filter=",headers=h)

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
        info_div = item.find("div", class_="info")
        hd_div = info_div.find("div", class_="hd")
        # span_class = hd_div.a.span.text
        # print(span_class)
        # spans = hd_div.select('span')[1].get_text()
        # print(spans)
        bd_div = item.find("div", class_="bd")
        quote_div = bd_div.find("p", class_="quote")
        quote = quote_div.text
        # quote_div = item.find('span', class_="inq")
        # quotes = quote_div.span
        print(quote)

        # for span in spans:
        #     text = span.text
        #     print(text,end="||")

        # bd_div = item.find("div", class_="bd")
        # a = bd_div.find('p',class_="")
        # print(a.text)

        # star_div = item.find("div", class_="star")
        # span_star = star_div.find('span',class_="rating_num")
        # print(span_star.text)

        # Number_evaluators = star_div.find('span',class_='',content="", property="")
        # print(Number_evaluators.text)

        # p = item.find('p',class_="quote")
        # quote = p.find('span',class_='inq')
        # print(quote.text)

        # span_2 = hd_div.find('span', class_='other')
        # Hongkong_Taiwan = span_2.text
        # print(Hongkong_Taiwan)

        # with connection.cursor() as cursor:
        #     # Create a new record
        #     sql = "INSERT INTO `movie_info` (`movie_name`, `movie_url`) VALUES (%s, %s)"
        #     cursor.execute(sql, (name,url))
    #
    #      # connection is not autocommit by default. So you must commit to save
    #     # your changes.
    # connection.commit()