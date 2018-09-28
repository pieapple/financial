# -*- coding:utf-8 -*-
import urllib
from datetime import date, timedelta
import xml.etree.cElementTree as ET
import xlwt

# url="http://cffex.com.cn/ccpm/?productid=T"

def retrieve_data(url):
    res = urllib.urlopen(url)
    text = res.read()
    try:
        root = ET.fromstring(text)
        return root
    except Exception as e:
        return None


def add_row(ws, index, date, root):
    ws.write(index, 0, date)
    ws.write(index, 1, root[-2][2].text)
    ws.write(index, 2, root[1][4].text)
    ws.write(index, 3, root[2][4].text)

wb = xlwt.Workbook()
ws = wb.add_sheet("summary")
ws.write(0, 0, "date")
ws.write(0, 1, "volume amount")
ws.write(0, 2, "largest buyer")
ws.write(0, 3, "largest seller")

row = 0
start_date = date(2015, 7, 1)
#end_date = date(2015, 8, 1)
end_date = date.today()
for n in range(int ((end_date - start_date).days)):
    single_date = start_date + timedelta(n)

    url = single_date.strftime("http://cffex.com.cn/sj/ccpm/%Y%m/%d/T.xml")
    root = retrieve_data(url)
    if root is None:
        continue

    date = single_date.strftime("%Y-%m-%d")
    row += 1
    print "adding row", row, date
    add_row(ws, row, date, root)

wb.save("financial_data.xls")
