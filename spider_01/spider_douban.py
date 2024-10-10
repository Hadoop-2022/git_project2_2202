import urllib.request
from bs4 import BeautifulSoup
import pymysql.cursors
import time

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='spider2202_douban',
                             cursorclass=pymysql.cursors.DictCursor)

#伪装头信息
h={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

with connection:
    for i in range(0,226,25):
        url = "https://movie.douban.com/top250?start="+str(i)+"&filter="
        request = urllib.request.Request(url, headers=h)
        r = urllib.request.urlopen(request)
        soup = BeautifulSoup(r.read().decode(), 'html.parser')
        items = soup.find_all("div", class_="item")


        for item in items:
            #海报、名字
            pic_div = item.find("div", class_="pic")
            img = pic_div.a.img
            poste = img['src']
            name = img['alt']

            # 中文名字
            info_div = item.find("div",class_="info")
            hd_div = info_div.find("div",class_="hd")
            span_1 = hd_div.find('span', class_='title')
            chinese_name = span_1.text

            # 英文名
            english_name = hd_div.select('span')[1].get_text()

            # 港台
            span_2 = hd_div.find('span', class_='other')
            Hongkong_Taiwan = span_2.text


            #详细
            bd_div = item.find("div", class_="bd")
            p = bd_div.find('p', class_="")
            Detailed_explanation = p.text

            # 评分
            star_div = item.find("div",class_="star")
            span_star = star_div.find('span',class_="rating_num")
            Score = span_star.text

            #评价人数
            span_4 = star_div.find('span',class_='',content="", property="")
            Number_evaluators = span_4.text

            #名言
            # quote_div = item.find('p', class_="quote")
            # quotes = quote_div.span
            quote_div = bd_div.find("p",class_="quote")
            if (quote_div):
                quote= quote_div.text
            else:
                quote=None


            with connection.cursor() as cursor:
                        # Create a new record
                sql = "INSERT INTO `douban_top250` (`movie_poster`,`movie_name`,`Chinese_name`,`English_name`,`Hongkong_Taiwan`,`Detailed_explanation`,`Score`,`Number_evaluators`,`Quote`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (poste,name,chinese_name,english_name,Hongkong_Taiwan,Detailed_explanation,Score,Number_evaluators,quote))

                cursor.close()

            # connection is not autocommit by default. So you must commit to save
            # your changes.
        connection.commit()

