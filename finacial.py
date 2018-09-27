# -*- coding:utf-8 -*-
import urllib

# url="http://cffex.com.cn/ccpm/?productid=T"
# res = urllib.urlopen(url)
# print res.read()

url="http://cffex.com.cn/sj/ccpm/201507/01/T.xml"
res = urllib.urlopen(url)
print res.read()
