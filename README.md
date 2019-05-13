# CrawlMaster_word
a word crawl master which can gather the following information: meaning, phonetic symbol, example, audio 
本次爬虫主要是为了收集单词数据用于背单词小程序的后台数据库构建
爬取的网页如下：
有道词典：http://dict.youdao.com/w/eng/key/#keyfrom=dict2.index
扇贝单词：https://www.shanbay.com/wordbook/205949/
爬取的信息：单词、释义、音标、发音、例句及例句中文翻译



学习python爬虫并实战的心得
1、正则表达式运用
2、json格式文件加载。
	json.dumps 用于将 Python 对象编码成 JSON 字符串
	json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
	dump与load 提供了操作文件读写的功能
3、本次实战中爬取的单词。对于4级单词、6级单词中存在交集的现象
  在爬取释义之前，求差集，避免重复爬取
4、爬虫获取数据避免给对方服务器增加太多负担。
  本次爬虫中，随机10秒内爬取一次。并在爬取30到100个单词后，随机休息50到120秒
5、因为数据量少，本次项目爬取时间在1000个单词1个小时左右。
  如想加快速度，可以采用IP池的方式(之后学习后会更新)
	
