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


def add_sheet(wb, sheet_name, root):
    ws = wb.add_sheet(sheet_name)
    row = 0
    for item in root:
        if item.tag != "data":
            break

        if row == 0:
            col = 0
            for field in item:
                ws.write(row, col, field.tag.strip())
                col += 1
            row += 1

        col = 0
        for field in item:
            ws.write(row, col, field.text.strip())
            col += 1
        row += 1


wb = xlwt.Workbook()

start_date = date(2018, 9, 20)
end_date = date.today()

for n in range(int ((end_date - start_date).days)):
    single_date = start_date + timedelta(n)

    url = single_date.strftime("http://cffex.com.cn/sj/ccpm/%Y%m/%d/T.xml")
    root = retrieve_data(url)
    if root is None:
        continue

    sheet_name = single_date.strftime("%Y-%m-%d")
    print "adding sheet", sheet_name
    add_sheet(wb, sheet_name, root)

wb.save("financial_data.xls")
