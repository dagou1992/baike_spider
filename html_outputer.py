#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'King'

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        data = new_data
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write("<td><a href=%s>" % data['url'])
            fout.write('%s</a></td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()