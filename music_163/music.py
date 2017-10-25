import requests
import time
import pymysql
from lxml import etree
from urllib.parse import urljoin

db = pymysql.connect(host="127.0.0.1", user="root", password="password", db="music163", charset="utf8")
cursor = db.cursor()


def open_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                            Chrome/61.0.3163.79 Safari/537.36'}
    req = requests.get(url, headers)
    req.encoding = 'utf-8'
    selector = etree.HTML(req.text)

    return selector


def songer():
    url = 'http://music.163.com'
    selector = open_url('http://music.163.com/discover/artist')
    leixing_href = selector.xpath('//div[@class="blk"]/ul/li/a/@href')
    leixing_name = selector.xpath('//div[@class="blk"]/ul/li/a/text()')
    for (href, leixing) in zip(leixing_href, leixing_name):
        print('获取：', leixing)
        url_word = urljoin(url, href)
        word_list = open_url(url_word).xpath('//ul[@id="initial-selector"]/li/a/@href')[1:]
        for words in word_list:
            url_name = urljoin(url, words)
            songer_name = open_url(url_name).xpath('//ul[@id="m-artist-box"]/li/p/a/text()|\
                                                    //ul[@id="m-artist-box"]/li/a/text()')
            songer_url = [urljoin(url, href[1:]) for href in open_url(url_name).xpath(
                        '//ul[@id="m-artist-box"]/li/p/a[1]/@href|//ul[@id="m-artist-box"]/li/a[1]/@href')]
            # 数据库插入、字段 songer_name, songer_url, leixing
            for (name, url) in zip(songer_name, songer_url):
                sql_insert = "INSERT INTO songer(songer_name, songer_url, songer_leixing) VALUES (%s, %s, %s)"
                cursor.execute(sql_insert, (name, url, leixing))
                db.commit()
        time.sleep(10)


def main():
    songer()


if __name__ == '__main__':
    main()
