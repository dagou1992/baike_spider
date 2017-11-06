#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider_main'

__author__ = 'King'

import html_downloader, html_outputer, html_parser, url_manager

class SpiderMain(object):
    def __init__(self):

        # url管理器
        self.urls = url_manager.UrlManager()

        # 下载器
        self.downloader = html_downloader.HtmlDownloader()

        # 解析器
        self.parser = html_parser.HtmlParser()

        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1

        # 初始url
        self.urls.add_new_url(root_url)

        # 当存在可爬取的url时
        while self.urls.has_new_url():
            try:
                # 获取待爬取url
                new_url = self.urls.get_new_url()

                print('craw %d: %s' % (count, new_url))

                # 启动下载器下载页面
                html_cont = self.downloader.download(new_url)

                # 启动解析器将新的url和爬到的数据进行保存
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                # 将新的url添加
                self.urls.add_new_urls(new_urls)

                # 收集爬取数据
                self.outputer.collect_data(new_data)

                # 爬取5个网页
                if count == 5:
                    break
                count += 1

            except:
                print('craw failed')

        # 输出内容
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()

    # start spider
    obj_spider.craw(root_url)