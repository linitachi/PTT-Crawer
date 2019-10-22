from crawler import PTTCrawler
import urllib
import requests


class Search(PTTCrawler):

    def __init__(self):
        pass

    def search_for_keyword(self, url, keyword='sony'):
        '''
        :param url 個版的網址
        :param keyword 想搜尋的文字
        '''
        search_endpoint_url = url + '/search'
        resp = requests.get(search_endpoint_url, params={'q': keyword})
        return self.transferto_Metadata(resp)

    def search_for_author(self, url, keyword=''):
        '''
        :param url 個版的網址
        :param keyword 想搜尋的作者
        '''
        search_endpoint_url = url + '/search'
        resp = requests.get(search_endpoint_url, params={
                            'q': 'author:'+keyword})
        return self.transferto_Metadata(resp)
