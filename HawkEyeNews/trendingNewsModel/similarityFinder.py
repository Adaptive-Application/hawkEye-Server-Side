import gensim
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
import operator
import requests
from .models import trendingNews


class simFinder():

    def __init__(self):
        self.tagName = []
        self.tagCode = []

    def rawDocument(self, file='../newsCorpora.json'):
        doc = []
        j = 0
        corpora = json.load(open(file, encoding="utf-8"))
        for i in corpora["corpora"]:
            doc.append(i["content"])
            self.tagName.append(i["tag"])
            self.tagCode.append(i["code"])
            j = j+1

        return doc

    def tfIdfModel(self, doclist, q):
        tokenizeWord = [[w.lower() for w in word_tokenize(text)]
                    for text in doclist]
        gen_docs = [[],[],[],[],[]]
        stopWords = set(stopwords.words('english'))
        stopWords.add(",")
        stopWords.add(".")
        stopWords.add("?")
        stopWords.add("(")
        stopWords.add(")")
        stopWords.add("'")
        stopWords.add("1")
        stopWords.add("2")
        stopWords.add("3")
        stopWords.add("4")
        stopWords.add("5")
        stopWords.add("6")
        stopWords.add("9")
        stopWords.add("10")
        j = 0
        for l in tokenizeWord:
            for w in l:
                if w not in stopWords:
                    gen_docs[j].append(w)
            j = j+1
        dictionary = gensim.corpora.Dictionary(gen_docs)
        corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
        tf_idf = gensim.models.TfidfModel(corpus)
        sims = gensim.similarities.Similarity('similarity', tf_idf[corpus],
                                              num_features=len(dictionary))
        query = [w.lower() for w in word_tokenize(q)]
        query_doc =[]
        for w in query:
            if w not in stopWords:
                query_doc.append(w)
        query_doc_bow = dictionary.doc2bow(query_doc)
        query_doc_tf_idf = tf_idf[query_doc_bow]
        similerityList = sims[query_doc_tf_idf]
        return similerityList

    def findSimilarity(self, query=''):

        sim = self.tfIdfModel(self.rawDocument('newsCorpora.json'), query)
        index, value = max(enumerate(sim), key=operator.itemgetter(1))
        tag = self.tagName[index]
        tagCode = self.tagCode[index]
        return tag, tagCode

    def executer(self):

        url = "http://webhose.io/filterWebContent?token=6ec4ce0d-1e01-4a84-8cdd-5bded9c3167d&format=json&ts=1522371266125&sort=social.facebook.shares&q=%22headlines%22%20thread.country%3AIE%20site_type%3Anews"
        req = requests.get(url=url)
        data = req.json()
        for i in range(10):
            q = data['posts'][i]['thread']['title_full']
            tag, tagCode = self.findSimilarity(query=q)
            trendingNews.objects.create(newsTag=tag, newsTagCode=tagCode, newsUrl= data['posts'][i]['thread']['url'])









