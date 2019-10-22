import crawler
import pretty_print
import time
import search
import save_to_excel
if __name__ == '__main__':
    pages = 1
    start = time.time()
    PTTcrawler = crawler.PTTCrawler()
    PT = pretty_print.PrettyPrint()
    searchItem = search.Search()
    Savecsv = save_to_excel.Savefile('index.csv')
    start_url = 'https://www.ptt.cc/bbs/mobilesales/index.html'

    # metadata = searchItem.search_for_keyword(
    #     "https://www.ptt.cc/bbs/movie", '三')
    # metadata = searchItem.search_for_author(
    #     "https://www.ptt.cc/bbs/movie", 'Tsai07')
    metadata = PTTcrawler.get_paged_meta(start_url, num_pages=pages)
    resps = PTTcrawler.get_posts(metadata)
    for resp in resps:
        data = PTTcrawler.get_page_content(resp)
        if data != 0:
            Savecsv.savetocsv(data)
