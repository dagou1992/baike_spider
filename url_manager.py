#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'King'


class UrlManager(object):

    def __init__(self):

        # 将url保存到内存中
        self.new_urls = set()
        self.old_urls = set()

    # 控制url存储到内存的函数
    def add_new_url(self, root_url):
        url = root_url
        if url is None:
            return

        # 如果这个url既不在待爬取的url中也不在爬取过的url中说明它是一个新的url
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 处理爬取到新的url的函数
    def add_new_urls(self, new_urls):
        urls = new_urls
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):

        # 获取一个新的url,在new_urls中删除，在old_urls中添加
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url