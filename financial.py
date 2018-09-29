# -*- coding:utf-8 -*-
from datetime import date, timedelta
from tqdm import tqdm
import urllib
import xml.etree.cElementTree as ET
import xlwt

# url="http://cffex.com.cn/ccpm/?productid=T"

def retrieve_data(url):
    res = urllib.urlopen(url)
    if res.code != 200:
        return None

    try:
        text = res.read()
        root = ET.fromstring(text)
        return root
    except Exception as e:
        return None


def add_header(ws):
    ws.write(0, 0, "date")
    ws.write(0, 1, "position")
    ws.write(0, 2, "volume amount")
    ws.write(0, 3, "largest buyer")
    ws.write(0, 4, "largest seller")


def add_row(ws, index, date, root):
    ws.write(index, 0, date)
    ws.write(index, 2, int(root[-2][2].text))
    ws.write(index, 3, root[1][4].text)
    ws.write(index, 4, root[2][4].text)


wb = xlwt.Workbook()
ws = wb.add_sheet("summary")
add_header(ws)

row = 0
start_date = date(2015, 7, 1)
end_date = date.today()

for n in tqdm(range(int ((end_date - start_date).days))):
    single_date = start_date + timedelta(n)

    url = single_date.strftime("http://cffex.com.cn/sj/ccpm/%Y%m/%d/T.xml")
    root = retrieve_data(url)
    if root is None:
        continue

    date = single_date.strftime("%Y-%m-%d")
    row += 1
    add_row(ws, row, date, root)

wb.save("result.xls")
