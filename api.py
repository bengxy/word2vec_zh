from gensim.models import Word2Vec
import sys
model = Word2Vec.load('my.model')
def w(target):
	try:
		tup = model.similar_by_word(target)
	except:
		raise
	for i in tup:
		print(i[0], ' ', i[1])


if __name__ == '__main__':
	while True:
		x = input('Input Chinese Words:')
		if not x:
			continue
		if x=='q':
			break
		try:
			w(x)
		except:
			print(sys.exc_info()[0])




