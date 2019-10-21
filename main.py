import crawler
import pretty_print
import time
if __name__ == '__main__':
    pages = 5
    start = time.time()
    PTTcrawler = crawler.PTTCrawler()
    PT = pretty_print.PrettyPrint()
    start_url = 'https://www.ptt.cc/bbs/movie/index.html'
    metadata = PTTcrawler.get_paged_meta(start_url, num_pages=pages)
    resps = PTTcrawler.get_posts(metadata)
    print('花費: %f 秒' % (time.time() - start))
    print('共%d項結果：' % len(resps))
    # for meta in metadata:
    #     PT.pretty_print(meta['push'], meta['title'],
    #                     meta['date'], meta['author'])
