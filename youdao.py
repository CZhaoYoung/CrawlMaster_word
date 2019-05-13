#!/usr/bin/env python
# utf-8
import urllib.request
import re
import sys

if len(sys.argv) == 1:
    print("要查找的单词")
    sys.exit()

word = ""
for x in range (len(sys.argv) - 1):
    word += "" + sys.argv[x+1]
print("单词 " + word)

URL = "http://dict.youdao.com/w/eng/" + word + "/#keyfrom=dict2.index"
response = urllib.request.urlopen(URL).read()      #获得网页源码
response=response.decode("utf-8", "ignore")
# 从源码中提取出单词释义的部分
searchSuccess = re.search(r"(?s)<div class=\"trans-container\">.*?<ul>.*?</div>", response)

if searchSuccess:
    means = re.findall(r"(?m)<li>(.*?)</li>", searchSuccess.group())
    print("释义")
    for mean in means:
        print("\t" + mean)  # 输出释义
else:
    print("未查到释义")
