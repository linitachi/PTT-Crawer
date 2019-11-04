from crawler import PTTCrawler
import save_to_excel
import search


class CrawlerProcessor(PTTCrawler):
    def __init__(self, file_name):
        self._file_name = file_name
        self.__Savecsv = save_to_excel.SaveToExcel(self._file_name)
        self.__Search = search.Search()

    def saveAll(self, start_url, pages):
        # save all item
        metadata = self.get_paged_meta(start_url, num_pages=pages)
        resps = self.get_posts(metadata)
        for resp in resps:
            data = self.get_page_content(resp)
            if data != 0:
                self.__Savecsv.savetocsv(data)

    def saveKeyword(self, start_url, pages, keyword):
        # save certain item by keyword
        metadata = self.__Search.search_for_keyword(
            start_url, keyword=keyword, page=pages)
        resps = self.get_posts(metadata)
        for resp in resps:
            data = self.get_page_content(resp)
            if data != 0:
                self.__Savecsv.savetocsv(data)


if __name__ == '__main__':
    a = CrawlerProcessor('inc.csv')
    pages = 2
    start_url = 'https://www.ptt.cc/bbs/mobilesales'
    a.saveKeyword(start_url, 2, 'sony')
