import time
from urllib.parse import urljoin

import requests
import pymysql
from lxml import etree
from fake_useragent import UserAgent


class MusicDB:
    def __init__(self):
        self.db = pymysql.connect(host="127.0.0.1", user="root", password="password", db="music163", charset="utf8")
        self.cursor = self.db.cursor()

    def insert_db(self, name, url, singer_type):
        sql_insert = "INSERT INTO singer(name, url, singer_type) VALUES (%s, %s, %s)"
        self.cursor.execute(sql_insert, (name, url, singer_type))
        self.db.commit()


class MusicSpider:
    def __init__(self):
        self.headers = {'User-Agent': UserAgent().random}

    def get_url(self, url):
        response = requests.get(url, self.headers)
        response.encoding = 'utf-8'
        selector = etree.HTML(response.text)
        return selector

    def singer(self):
        """歌手"""
        md = MusicDB()
        url = 'http://music.163.com'
        selector = self.get_url('http://music.163.com/discover/artist')
        singer_type_href = selector.xpath('//div[@class="blk"]/ul/li/a/@href')
        singer_type_name = selector.xpath('//div[@class="blk"]/ul/li/a/text()')
        for (href, type_name) in zip(singer_type_href, singer_type_name):
            print('获取：', type_name)
            url_word = urljoin(url, href)
            word_list = self.get_url(url_word).xpath('//ul[@id="initial-selector"]/li/a/@href')[1:]
            for words in word_list:
                url_name = urljoin(url, words)
                singer_name = self.get_url(url_name).xpath('//ul[@id="m-artist-box"]/li/p/a/text()|\
                                                        //ul[@id="m-artist-box"]/li/a/text()')
                singer_url = [urljoin(url, href[1:]) for href in self.get_url(url_name).xpath(
                    '//ul[@id="m-artist-box"]/li/p/a[1]/@href|//ul[@id="m-artist-box"]/li/a[1]/@href')]
                for (name, url) in zip(singer_name, singer_url):
                    md.insert_db(name, url, type_name)
            time.sleep(10)


if __name__ == '__main__':
    """
    rest"""
    ms = MusicSpider()
    ms.singer()
