#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'King'

import xlwt

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        data = new_data
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):

        # fout = open('output.html', 'w', encoding='utf-8')
        # fout.write('<html>')
        # fout.write('<body>')
        # fout.write('<table>')
        #
        # for data in self.datas:
        #     fout.write('<tr>')
        #     fout.write("<td><a href=%s>" % data['url'])
        #     fout.write('%s</a></td>' % data['title'])
        #     fout.write('<td>%s</td>' % data['summary'])
        #     fout.write('</tr>')
        #
        # fout.write('</table>')
        # fout.write('</body>')
        # fout.write('</html>')
        # fout.close()

        print('准备将数据存入表格...')

        book = xlwt.Workbook()
        sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)

        # 先将表头保存
        heads = [u'No', u'title', u'summary', u'url']
        ii = 0
        for head in heads:
            sheet1.write(0, ii, head)
            ii += 1

        # 导入数据
        i = 1
        for data in self.datas:
            sheet1.write(i, 0, i)
            sheet1.write(i, 1, data['title'])
            sheet1.write(i, 2, data['summary'])
            sheet1.write(i, 3, data['url'])
            i += 1

        book.save('Python_Baike_Data.xls')
        print('保存成功')