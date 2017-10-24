import requests
from lxml import etree


def url_open(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/61.0.3163.79 Safari/537.36'}
    req = requests.get(url, headers=header)
    req.encoding = 'utf-8'
    selector = etree.HTML(req.text)

    return selector


# 从热门50单曲页面获取所有专辑的链接
def all_album(url):
    selector = url_open(url)
    all_album_href = ''.join(selector.xpath('//ul[@id="m_tabs"]/li[2]/a/@href'))
    song_url = 'http://music.163.com' + all_album_href

    return song_url


# 所有专辑信息
def album_info(name, href, time):

    # return album_name
    pass


# 获取所有专辑的链接
def zhuanji(url):
    selector = url_open(url)
    name = selector.xpath('//ul[@id="m-song-module"]/li/p[1]/a/text()')
    href = selector.xpath('//ul[@id="m-song-module"]/li/p[1]/a/@href')
    time = selector.xpath('//ul[@id="m-song-module"]/li/p[2]/span/text()')
    [album_name.append(i) for i in name]
    [album_href.append(i) for i in href]
    [album_time.append(i) for i in time]
    next_page_href = selector.xpath('//div[@class="u-page"]/a/@href')
    if next_page_href[-1] != 'javascript:void(0)':
        pages = 'http://music.163.com' + next_page_href[-1]
        zhuanji(pages)


def main():
    url = 'https://music.163.com/artist?id=1876'
    urls = all_album(url)
    global album_name, album_href, album_time
    album_name = []
    album_href = []
    album_time = []
    zhuanji(urls)



if __name__ == '__main__':
    main()
