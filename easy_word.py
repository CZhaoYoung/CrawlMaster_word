# 爬取4000多个基本词，用于词向量构建

import json
import re
import urllib.request
import time
import random


with open("D:/EasyWord", 'r') as load_f:
    data = json.load(load_f)

global count
count = 0

# 创建单词字典，以英文单词为键，拥有多个属性。
# means，释义；mark，音标；audio，发音；Synonyms，同义词；example，例句。
# 首先完成前三个属性的爬取

dictionary = {'Wid': '', 'name': '', 'meaning': '', 'soundmark': '', 'sentence': '', 'sentenceMeaning': '', 'audioUrl': ''}
headers = {"User-Agent", "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}

# 创建open对象
opener = urllib.request.build_opener()
# 把opener对象下的addheader属性设置为相关的用户代理信息
opener.addheaders=[headers]
# 安装后，urllib.request 也能以浏览器身份访问
urllib.request.install_opener(opener)


for key in data:
    dictionary['name'] = key
    URL = "http://dict.youdao.com/w/eng/" + key + "/#keyfrom=dict2.index"
    response = urllib.request.urlopen(URL).read()  # 获得网页源码
    response = response.decode("utf-8", "ignore")
    # 从源码中提取出单词释义的部分
    searchSuccess1 = re.search(r"(?s)<div class=\"trans-container\">.*?<ul>.*?</div>", response)
    if searchSuccess1:
        means = re.findall(r"(?m)<li>(.*?)</li>", searchSuccess1.group())
    dictionary['meaning'] = means
    # dictionary.setdefault(key, []).append(means[0])

    # 爬取音标
    searchSuccess2 = re.search(r"(?s)<div class=\"baav\">.*?美.*?</span>", response)
    if searchSuccess2:
        answer = re.findall(r"\[.*?\]", searchSuccess2.group())
        mark = answer[0]  # 选取美式音标
    dictionary['soundmark'] = mark

    # 爬取例句
    searchSuccess3 = re.search(r"(?s)<div class=\"examples\">.*?</div>", response)
    if searchSuccess3:
        answer = re.findall(r"(?m)<p>(.*?)</p>", searchSuccess3.group())
        example = answer[0]
        sentenceMeaning = answer[1]
    dictionary['sentence'] = example
    dictionary['sentenceMeaning'] = sentenceMeaning

    print(key, means[0], mark, example, sentenceMeaning)

    # 爬取音频
    audio_url = "http://dict.youdao.com/dictvoice?audio=" + key + "&type=1"
    dictionary['audioUrl'] = audio_url
    count += 1
    dictionary['Wid'] = 13999 + count
    # 保存数据中存在中文格式因此需要考虑编码
    with open("WordList.json", 'a', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False)
        f.write('\n')  # 写入换行符

    time.sleep(random.randint(1, 8))
    if count == 5:
        print("wonderful")
    if (count == 30)|(count == 70)|(count == 110)|(count == 140)|(count == 190)|(count == 250)|(count == 300)|(count == 340)|(count == 370)|(count == 410):
        print("sleeping")
        time.sleep(random.randint(60,120))
    if (count == 460)|(count == 510)|(count == 561)|(count == 600)|(count == 660)|(count == 720)|(count == 799)|(count == 840):
        print("sleeping")
        time.sleep(random.randint(60,120))
    if (count == 900)|(count == 950)|(count == 1000)|(count == 1050)|(count == 1100)|(count == 1150)|(count == 1200)|(count == 1300):
        print("sleeping")
        time.sleep(random.randint(100,200))
    if (count == 1350)|(count == 1400)|(count == 1450)|(count == 1500)|(count == 1550)|(count == 1601)|(count == 1650)|(count == 1700):
        print("sleeping")
        time.sleep(random.randint(100,200))
    if (count == 1750)|(count == 1800)|(count == 1850)|(count == 1900)|(count == 1950)|(count == 2000)|(count == 2050)|(count == 2100):
        print("sleeping")
        time.sleep(random.randint(100,200))
    if (count == 2200)|(count == 2300)|(count == 2400)|(count == 2450)|(count == 2500)|(count == 2550)|(count == 2600)|(count == 2650)|(count == 2700):
        print("sleeping")
        time.sleep(random.randint(100,200))
print('done!!')