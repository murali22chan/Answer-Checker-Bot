import gensim
from gensim.matutils import softcossim 
from gensim import corpora
import gensim.downloader as api
from gensim.utils import simple_preprocess


#Loading the fasttext_model
fasttext_model300 = api.load('fasttext-wiki-news-subwords-300')

#Function to execute the soft cosine similarity, take two string argument and return a float value between 0 to 1
def similarity_score(doc1 , doc2):
	documents = [doc1, doc2]

	dictionary = corpora.Dictionary(simple_preprocess(doc) for doc in documents)

	similarity_matrix = fasttext_model300.similarity_matrix(dictionary, tfidf=None, threshold=0.0, exponent=2.0, nonzero_limit=100)

	sentence1 = dictionary.doc2bow(simple_preprocess(doc1))

	sentence2 = dictionary.doc2bow(simple_preprocess(doc2))

	sentences = [sentence1, sentence2]

	return softcossim(sentence1, sentence2, similarity_matrix)


