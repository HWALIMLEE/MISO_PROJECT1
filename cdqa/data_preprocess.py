import os
import pandas as pd
import csv
import re
from ast import literal_eval
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.evaluation import f1_score, exact_match_score

# dataset
df = pd.read_csv('./data/data_augmentation.csv', converters={'paragraphs': literal_eval},encoding='utf-8')
# paragraphs 새로 정의 : Title + Paragraph
df['paragraphs_old'] = df['paragraphs']
df['paragraphs'] = df.apply(lambda row: [row['title']] + row['paragraphs_old'], axis=1).copy()

data = pd.read_csv('./data/data_augmentation.csv',encoding='utf-8')
data_sampling = data.sample(100,random_state=66)

from cdqa.retriever import TfidfRetriever, BM25Retriever
cdqa_pipeline = QAPipeline(reader='bert_qa_multi_epoch3.joblib', retrieve_by_doc=True,retriever='bm25')
cdqa_pipeline.fit_retriever(df=df)
cdqa_pipeline.cuda()
retriever = BM25Retriever(ngram_range=(1,2), max_df=0.8, min_df=3, stop_words=None,lowercase=True, top_n=5)
retriever.fit(df=df)
def f1(dataframe,dataframe2):
    number = 0
    exact_number = 0
    # score = []
    answer_list=[] 
    while number < 100:
        # print("Question?")
        question = dataframe2.iloc[number,2] # 질문
        # question = input()
        best_idx_scores = retriever.predict(question)
        prediction = df.loc[best_idx_scores.keys()]['paragraphs'].apply(lambda x:x[1]).tolist()[0].replace(u'\xa0',u'')
        number+=1
        answer_list.append(prediction)
    return answer_list

mylist=f1(df,data_sampling)
data_sampling['prediction'] = mylist # 리스트는 바로 pandas.dataframe 데이터로 넣어줄 수 있음
text = data_sampling['paragraphs'].apply(lambda x: re.sub('[[]','',x)).apply(lambda x:re.sub('[]]','',x))
data_sampling['paragraphs'] = text
data_sampling.to_csv('./data/data_augmentation_complete(66).csv')

