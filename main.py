import crawler
import pretty_print
import time
import search
if __name__ == '__main__':
    pages = 5
    start = time.time()
    PTTcrawler = crawler.PTTCrawler()
    PT = pretty_print.PrettyPrint()
    searchItem = search.Search()
    start_url = 'https://www.ptt.cc/bbs/movie/index.html'

    # metadata = searchItem.search_for_keyword(
    #     "https://www.ptt.cc/bbs/movie", '三')
    # metadata = searchItem.search_for_author(
    #     "https://www.ptt.cc/bbs/movie", 'Tsai07')
    metadata = PTTcrawler.get_paged_meta(start_url, num_pages=pages)
    resps = PTTcrawler.get_posts(metadata)
    print('花費: %f 秒' % (time.time() - start))
    print('共%d項結果：' % len(resps))
    for meta in metadata:
        PT.pretty_print(meta['push'], meta['title'],
                        meta['date'], meta['author'])
