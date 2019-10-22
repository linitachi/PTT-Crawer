import crawler
import pretty_print
import time
import search
import crawler_process
if __name__ == '__main__':
    pages = 2
    start = time.time()
    Processor = crawler_process.CrawlerProcessor('index.csv')
    start_url = 'https://www.ptt.cc/bbs/mobilesales/index.html'
    Processor.saveAll(start_url, pages)
    print('花費: %f 秒' % (time.time() - start))
    # metadata = searchItem.search_for_keyword(
    #     "https://www.ptt.cc/bbs/movie", '三')
    # metadata = searchItem.search_for_author(
    #     "https://www.ptt.cc/bbs/movie", 'Tsai07')
