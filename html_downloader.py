#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'King'

from urllib import request

class HtmlDownloader(object):

    def download(self, new_url):
        url = new_url
        if url is None:
            return None
        res = request.urlopen(url)

        if res.getcode() != 200:
            return None

        return res.read()