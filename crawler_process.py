from crawler import PTTCrawler
import save_to_excel


class CrawlerProcessor(PTTCrawler):
    def __init__(self, file_name):
        self._file_name = file_name
        self.__Savecsv = save_to_excel.SaveToExcel(self._file_name)

    def saveAll(self, start_url, pages):
        metadata = self.get_paged_meta(start_url, num_pages=pages)
        resps = self.get_posts(metadata)
        for resp in resps:
            data = self.get_page_content(resp)
            if data != 0:
                self.__Savecsv.savetocsv(data)


if __name__ == '__main__':
    a = CrawlerProcessor('inc.csv')
    print(CrawlerProcessor.domain)
