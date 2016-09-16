# coding:utf-8
# 分词
import jieba
import os
import re

def load_stopwords():
	print('Load stopword_library...')
	stopfile = open('stopword.lib')
	stopwords_library = set([])
	while True:
		word = stopfile.readline()
		if not word:
			break
		stopwords_library.add(word)
	return stopwords_library

stopwords_library = load_stopwords()

def remove_stopwords(cut_origin=[]):
	'''
	WARNING >>>: 
	remove_stopwords() will change the input list as its using the ref to speedup
	'''
	for i in cut_origin:
		if i in stopwords_library:
			cut_origin.remove(i)
	


def preprocess(in_filename, out_filename):
	in_file = open(in_filename, 'r')
	out_file = open(out_filename,'a')
	while True:
		line = in_file.readline()

		if not line:
			break
		line = line.strip()
		if not line:
			continue
		#sep by punctuation
		#sentences = re.split('《', line)
		#sentences = re.split('。|？|！|\.|-|：| |（|）', line)
		sentence = line
		#for sentence in sentences:
		#	if not sentence:
		#		continue
		cut_res = jieba.lcut(sentence, cut_all=True)
		remove_stopwords(cut_res)
		if not cut_res:
			continue
		new_line = ' '.join(cut_res)+'\n'
		out_file.write(new_line)

	in_file.close()
	out_file.close()	



if __name__ == '__main__':
	data_dir = 'data/'
	cut_data_dir = 'cut_data/'
	#output_file_name = 'cut.txt'
	#output_file = open(output_file_name, 'a')
	files = os.listdir(data_dir)	

	for afile in files:
		if afile[0] == '.' || afile =='readme.md':
			continue
		print('Preprocessing...:', afile)
		preprocess(data_dir+afile, cut_data_dir + 'cut.txt')

	#output_file.close()