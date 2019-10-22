from crawler import PTTCrawler
import urllib
import requests
import time


class Search(PTTCrawler):

    def __init__(self):
        pass

    def requestResp(self, url, keyword, page):
        search_endpoint_url = url + '/search'
        resp = requests.get(search_endpoint_url, params={
                            'q': keyword, 'page': page})
        return resp

    def search_for_keyword(self, url, keyword='sony', page=1):
        '''
        :param url 個版的網址
        :param keyword 想搜尋的文字
        '''
        return self.transferto_Metadata(self.requestResp(url, keyword, page))

    def search_for_author(self, url, keyword=''):
        '''
        :param url 個版的網址
        :param keyword 想搜尋的作者
        '''
        keyword = 'author:'+keyword
        return self.transferto_Metadata(self.requestResp(url, keyword, page))

    # def search_for_date(self, url, keyword=''):
    #     '''
    #     :param url 個版的網址
    #     :param keyword 想搜尋的時間
    #     '''
    #     if keyword == '':
    #         localtime = time.localtime(time.time())
    #         keyword = str(localtime.tm_mon) + '/' + str(localtime.tm_mday)
