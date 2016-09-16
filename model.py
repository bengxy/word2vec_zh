# -*- coding:utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

import os

print('Load Sentences...')
cut_dir = 'cut_data/'
files_name = os.listdir(cut_dir)
sentences = LineSentence(cut_dir+'cut.txt')

print('Initial Model...')
model = Word2Vec(min_count=30, size=200)

print('Build Vocab...')
model.build_vocab(sentences)

for i in range(1):
	print('Train model, Step ', i)
	model.train(sentences)

model.save('my.model')




# for file_name in files_name:
# 	if file_name[0]=='.':
# 		continue
# 	print(file_name)
# 	#file_name = '东方.txt'
# 	final_sentences += LineSentence(cut_dir+file_name)
# 	if not vocab_builded:
# 		model.build_vocab(sentences)
# 		vocab_builded = True
# 	model.train(sentences)


	
