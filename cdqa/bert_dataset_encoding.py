#-*-coding:utf-8-*-
import pandas as pd
import csv
import re
data = pd.read_csv(r'C:\Users\hwali\korquad.github.io\bert_dataset.csv',encoding='utf-8')

def CleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', str(readData))
    return text

def List(sentence):
    new_sentence=[]
    new_sentence.append(sentence)
    return new_sentence

data['paragraphs']=data['paragraphs'].apply(lambda x: List(CleanText(x)))
print(data['paragraphs'])

data.to_csv('bert_dataset_prepro.csv')

# df2 = pd.read_csv('bert_dataset_prepro.csv')
# for paragraph in df2['paragraphs']:
#     print(type(paragraph))