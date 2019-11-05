import crawler
import pretty_print
import time
import search
import crawler_process
if __name__ == '__main__':
    pages = 2
    csvTitle = 'index.csv'
    keyword = 'u11'
    find_all = 0
    start = time.time()
    Processor = crawler_process.CrawlerProcessor(csvTitle)

    if find_all:
        # 如果要存全部檔案
        start_url = 'https://www.ptt.cc/bbs/mobilesales/index.html'
        Processor.saveAll(start_url, pages)
    else:
        # 如果要存特定關鍵字檔案
        start_url = 'https://www.ptt.cc/bbs/mobilesales/'
        Processor.saveKeyword(start_url, pages, keyword)
        print('花費: %f 秒' % (time.time() - start))
