# # -*- coding: utf-8 -*-
import os
import sys
import re
import MeCab
import collections
from gensim import models
from gensim.models.doc2vec import TaggedDocument

path = "dataset"


# 全てのファイルのリストを取得
def get_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield re.match('[0-9]+', format(file)).group()


# ファイルから文章を返す
def read_document(fn):
    with open(path + "/" + fn + ".txt", 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()


# 文章から単語に分解して返す
def split_into_words(doc, name=''):
    mecab = MeCab.Tagger("-Ochasen")
    # valid_doc = trim_doc(doc)
    lines = mecab.parse(doc).splitlines()
    words = []
    for line in lines:
        chunks = line.split('\t')
        if len(chunks) > 3 and (chunks[3].startswith('動詞') or chunks[3].startswith('形容詞') or (
                chunks[3].startswith('名詞') and not chunks[3].startswith('名詞-数'))):
            words.append(chunks[0])
    return TaggedDocument(words=words, tags=[name])


# ファイルから単語のリストを取得
def corpus_to_sentences(corpus):
    docs = [read_document(x) for x in corpus]
    for idx, (doc, name) in enumerate(zip(docs, corpus)):
        print('\r前処理中 {} / {}'.format(idx, len(corpus)))
        yield split_into_words(doc, name)


corpus = list(get_all_files(path))
sentences = list(corpus_to_sentences(corpus))

model = models.Doc2Vec(size=400, alpha=0.0015, sample=1e-4, min_count=1, workers=4)
model.build_vocab(sentences)

token_count = sum([len(sentence) for sentence in sentences])

for x in range(30):
    model.train(sentences, total_examples=token_count, epochs=10)
    ranks = []
    for doc_id in range(len(sentences)):
        inferred_vector = model.infer_vector(sentences[doc_id].words)
        sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
        rank = [docid for docid, sim in sims].index(sentences[doc_id].tags[0])
        ranks.append(rank)
        if collections.Counter(ranks)[0] >= 90:
            print('ok')
            model.save('doc2vec.model')
            break
    model.save('doc2vec.model')
