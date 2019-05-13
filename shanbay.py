# 抓取扇贝网中四六级大纲单词，共计7821个
#

import json
import re
import urllib.request
import time
import random

global count
count = 0

# 创建单词字典，以英文单词为键，拥有多个属性。
# means，释义；mark，音标；audio，发音；Synonyms，同义词；example，例句。
# 首先完成前三个属性的爬取

dictionary = []
headers = {"User-Agent", "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}

# 创建open对象
opener = urllib.request.build_opener()
# 把opener对象下的addheader属性设置为相关的用户代理信息
opener.addheaders=[headers]
# 安装后，urllib.request 也能以浏览器身份访问
urllib.request.install_opener(opener)

for n in range(0, 40):
    print("正在爬第" + str(n) + "本书")
    for i in range(1, 11):
        URL = "https://www.shanbay.com/wordlist/182800/" + str(516751 + 3 * n) + "/?page="
        URL += str(i)
        response = urllib.request.urlopen(URL).read()  # 获得网页源码
        response = response.decode("utf-8", "ignore")
        # 从源码中提取出单词释义的部分
        searchSuccess1 = re.search(r"(?s)<table class=\"table table-bordered table-striped\">.*?<tbody>.*?</tbody>", response)
        if searchSuccess1:
            word = re.findall(r"(?m)<strong>(.*?)</strong>", searchSuccess1.group())
            print(word)
            dictionary += word
        time.sleep(random.randint(2,5))

    time.sleep(random.randint(1, 10))
    count += 1
    if count == 1:
        print("wonderful")
    if (count == 5)|(count == 10)|(count == 15)|(count == 20)|(count == 25)|(count == 30)|(count == 35):
        print("sleeping")
        time.sleep(random.randint(100,200))


with open("word", 'w', encoding='utf-8') as f:
    json.dump(dictionary, f, ensure_ascii=False)
print('done!!')




