import requests
import time
import csv
import pymysql
from lxml import etree
db = pymysql.connect(host="127.0.0.1", user="root", password="password", db="music163", charset="utf8")
cursor = db.cursor()


def name_href():
    names = []
    hrefs = []
    urls = ['http://music.163.com/discover/artist/cat?id=1001', 'http://music.163.com/discover/artist/cat?id=1002',
            'http://music.163.com/discover/artist/cat?id=1003', 'http://music.163.com/discover/artist/cat?id=2001',
            'http://music.163.com/discover/artist/cat?id=2002', 'http://music.163.com/discover/artist/cat?id=2003',
            'http://music.163.com/discover/artist/cat?id=6001', 'http://music.163.com/discover/artist/cat?id=6002',
            'http://music.163.com/discover/artist/cat?id=6003', 'http://music.163.com/discover/artist/cat?id=7001',
            'http://music.163.com/discover/artist/cat?id=7002', 'http://music.163.com/discover/artist/cat?id=7003',
            'http://music.163.com/discover/artist/cat?id=4001', 'http://music.163.com/discover/artist/cat?id=4002',
            'http://music.163.com/discover/artist/cat?id=4003']
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/61.0.3163.79 Safari/537.36'}
    # with open('name_href.csv', 'a', encoding='utf-8') as f:
    #     f_csv = csv.writer(f, delimiter=',', lineterminator='\n')
    #     f_csv.writerow(["name", "href"])
    try:
        for url in urls:
            for i in range(65, 91):
                url_name = url + '&initial=' + str(i)
                req = requests.get(url_name, headers=header)
                selector = etree.HTML(req.text)
                name = selector.xpath('//ul[@id="m-artist-box"]/li/p/a[1]/text()|\
                                       //ul[@id="m-artist-box"]/li/a[1]/text()')
                href = selector.xpath('//ul[@id="m-artist-box"]/li/p/a[1]/@href|\
                                       //ul[@id="m-artist-box"]/li/a[1]/@href')
                [names.append(i) for i in name]
                [hrefs.append(i) for i in href]
            url_name = url + '&initial=0'
            req = requests.get(url_name, headers=header)
            selector = etree.HTML(req.text)
            print(url_name)
            name = selector.xpath('//ul[@id="m-artist-box"]/li/p/a[1]/text()|\
                                   //ul[@id="m-artist-box"]/li/a[1]/text()')
            href = selector.xpath('//ul[@id="m-artist-box"]/li/p/a[1]/@href|\
                                   //ul[@id="m-artist-box"]/li/a[1]/@href')
            [names.append(i) for i in name]
            [hrefs.append(i) for i in href]
            time.sleep(10)

    except Exception as e:
        print(str(e))
    print(names)
    print(hrefs)
    for (name, href) in zip(names, hrefs):
        sql_insert = "INSERT INTO songer(name, name_href) VALUES (%s, %s)"
        cursor.execute(sql_insert, (name, href))
        db.commit()


name_href()
