import time
from collections import OrderedDict
def predict(self,query:str)->OrderedDict:
    """
    Compute the top_n closet given a query
    
    Parameters
    -----------
    query:str

    Returns
    --------
    best_idx_scores: OrderedDict
        Dictionnaire with top_n best scores and idices of the documents as keys
    """
    t0 = time.time()
    scores = self._compute_scores(query)
    idx_scores = [(idx,score) for idx, score in enumerate(scores)]
    best_idx_scores = OrderedDict(sorted(idx_scores,key=(lambda tup:tup[1]),reverse=True)[:self.top_n])


    def _compute_scores(self, query):
        question_vector = self.vectorizer.transform([query], is_query=True) # BM25vectorizer
        scores = self.bm25_matrix.dot(question_vector.T).toarray()
        return scores

        # self.bm25_matrix = self.vectorizer.fit_transform(df['content'])
        # 우리의 df['content']는 현재paragraphs랑 똑같다.(paragraphs = question+ answer)
        # self.vectorizer = BM25Vectorizer --->벡터화 시키고
        # content vector 와 query vector 곱한 거
