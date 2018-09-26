# -*- coding:utf-8 -*-
import urllib2

# url="http://cffex.com.cn/ccpm/?productid=T"
# response = urllib2.urlopen(url)
# print response.read()

url="http://cffex.com.cn/sj/ccpm/201507/01/T.xml"
response = urllib2.urlopen(url)
print response.read()
