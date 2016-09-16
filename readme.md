# Zh-Word2Vec 中文Word2Vec  


选用历年《矛盾文学奖作品》为语料库，训练word vector

详细博客：[word2vec在中文数据集上的实验]()

## 项目说明  
### 数据集  

* 历年矛盾文学奖作品
* 数据下载地址 **(encoding = utf-8)**
	* [数据堂]() **(未处理 encoding = gb18030)**
	* [百度盘]() 
	* [dropbox]()
	* [个人服务器]()
* 数据存放说明（参考每个目录下的readme）
	* raw_data （**数据堂**的源数据存放位置；[可选] 文本编码：gb18030） 
	* data （其他来源的数据存放位置； 文本编码：utf-8）
	* cut_data （分词后的文本）

### 项目依赖库
* [gensim](https://radimrehurek.com/gensim/install.html) （word2vec） 
* [jieba](https://github.com/fxsjy/jieba) （分词）




### 运行说明
* coding.py (可选)
	* 如果使用数据堂数据，需要先做编码的encoding，把所有的txt文件放在raw_data里，运行coding.py即可在 `data/` 目录下生成转码的后的文本
* data_pre.py 
	* 数据预处理，读取 `data/` 下的txt文本，运行后会在 `cut_data/` 目录下生成分词后的结果，每行是一个句子，每句话的单词用空白符分割
* model.py
	* 训练word2vec模型，生成的模型会保存为根目录下的`my.model` 
* api.py 
	* 直接调用模型，用户输入中文词语，返回相似的词
* stopword.lib
	* 每行是一个stopword，可以自行添加和修改

## 结果

![image](http://oallcpxbv.bkt.clouddn.com/word2vec1.png)

![image](http://oallcpxbv.bkt.clouddn.com/word2vec2.png)


## 参考

具体说明参考： [word2vec在中文数据集上的实验]()



