import requests
from requests_html import HTML
import re
import time
import urllib
from multiprocessing import Pool
from bs4 import BeautifulSoup
import csv
from datetime import datetime


class PTTCrawler:
    domain = 'https://www.ptt.cc/'

    def __init__(self):
        self.domain = 'https://www.ptt.cc/'

    def fetch(self, url):
        response = requests.get(url)
        # 一直向 server 回答滿 18 歲了 !
        response = requests.get(url, cookies={'over18': '1'})
        return response

    def parse_article_entries(self, doc):
        html = HTML(html=doc)
        post_entries = html.find('div.r-ent')
        return post_entries

    def parse_article_meta(self, ent):
        '''
        每筆資料都存在 dict() 類型中：key-value paird data
        '''
        meta = {
            'title': ent.find('div.title', first=True).text,
            'push': ent.find('div.nrec', first=True).text,
            'date': ent.find('div.date', first=True).text,
        }
        try:
            meta['author'] = ent.find('div.author', first=True).text
            meta['link'] = ent.find('div.title > a', first=True).attrs['href']
        except AttributeError:
            if '(本文已被刪除)' in meta['title']:
                match_author = re.search('\[(\w*)\]', meta['title'])
                if match_author:
                    meta['author'] = match_author.group(1)
            elif re.search('已被\w*刪除', meta['title']):
                match_author = re.search('\<(\w*)\>', meta['title'])
                if match_author:
                    meta['author'] = match_author.group(1)
        return meta

    def get_metadata_from(self, url):

        def parse_next_link(doc):
            html = HTML(html=doc)
            controls = html.find('.action-bar a.btn.wide')
            link = controls[1].attrs.get('href')
            return urllib.parse.urljoin(self.domain, link)
        resp = self.fetch(url)
        next_link = parse_next_link(resp.text)
        metadata = self.transferto_Metadata(resp)
        return metadata, next_link

    def get_paged_meta(self, url, num_pages):
        collected_meta = []

        for _ in range(num_pages):
            posts, link = self.get_metadata_from(url)
            collected_meta += posts
            url = urllib.parse.urljoin(self.domain, link)

        return collected_meta

    def get_posts(self, metadata):
        # 將所有文章連結收集並串接成完整 URL
        post_links = [
            urllib.parse.urljoin(self.domain, meta['link'])
            for meta in metadata if 'link' in meta
        ]

        with Pool(processes=16) as pool:
            contents = pool.map(self.fetch, post_links)
            return contents

    def transferto_Metadata(self, resp):
        '''
        把結果轉成可讀的內容
        :param resp 網站的回應
        '''
        post_entries = self.parse_article_entries(resp.text)
        metadata = [self.parse_article_meta(entry) for entry in post_entries]
        return metadata

    def get_page_content(self, response):
        '''
        取得頁面的資料
        如果回傳0代表不是賣的人
        '''
        soup = BeautifulSoup(response.text, 'lxml')
        main_content = soup.find(id="main-content")
        metas = main_content.select('div.article-metaline')
        content = main_content.text
        number_start = content.find(u'欲售價格' or u'交易價格')
        number_end = content.find(u'\n', number_start)
        try:
            author = metas[0].select('span.article-meta-value')[0].string
            title = metas[1].select('span.article-meta-value')[0].string
        except IndexError as n:
            author = '??'
            title = '??'
        if(title[1] != '賣'):  # 如果不是賣 就返回0
            return 0
        date = metas[2].select('span.article-meta-value')[0].string
        price = content[number_start+5:number_end]
        link = main_content.select_one("span.f2 a")
        data = [[author, date, title.lower(), price, link.text]]
        return data


if __name__ == '__main__':
    aaa = PTTCrawler()
    start_url = 'https://www.ptt.cc/bbs/mobilesales/index.html'
    metadata = aaa.get_paged_meta(start_url, 1)
    resps = aaa.get_posts(metadata)
    for reaa in resps:
        bbb = aaa.get_page_content(reaa)
