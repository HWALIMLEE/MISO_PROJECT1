import json
from pprint import pprint
result=[]
with open('korquad2.1_train_00.json','r',encoding='utf-8')as json_file:
    json_data = json.load(json_file)
    print(json_data.keys())
    print(len(json_data['data'])) #1000
    # print(json_data['data'])
    # print('=======================================')
    # print(json_data['data'][0])
    # print('=======================================')
    # print(json_data['data'][1])
    # # print(json_data['data'][1]['paragraphs'][0]['qas'][0]['answers'])
    # print('=======================================')
    # print(json_data['data'][2])
    # print('=======================================')
    # print(json_data['data'][3])
    # print('=======================================')
    # print(json_data['data'][4])
    print('=======================================')
    print(json_data['data'][1].keys()) #['title', 'url', 'context', 'raw_html', 'qas']
    print(json_data['data'][1]['title']) # 심규언
    print('=======================================')
    print(json_data['data'][1]['url']) # https://ko.wikipedia.org/wiki/심규언
    print('=======================================')
    print(json_data['data'][1]['raw_html']) # 여기만 잘 손보면 될 것 같은데
    print('=======================================')
    print(json_data['data'][1]['qas'][0].keys()) 
    print(json_data['data'][1]['qas'][0]['answer'].keys())
    print(json_data['data'][1]['qas'][0])
    #[{'answer': {'text': '20,890 표', 'html_answer_start': 16093, 'html_answer_text': '20,890 표', 'answer_start': 3873}, 'question': '심규언은 17대 지방 선거에서 몇 표를 득표하였는가?', 'id': '36615'}]
    print('=======================================')
    print(json_data['data'][1]['context'])

# 한글만 가져오는 정규식 사용
#-*- coding:utf-8-*-
import re
articles_array=[]
def test(text):
    symbol = re.compile('(<([^>]+)>)')
    english = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = symbol.sub('',text)
    result = english.sub('',text)
    articles_array.append(result)
    for article in articles_array:
        if '\n' in articles_array:
            articles_array.remove('\n')
    return articles_array
    # print(type(articles_array))

print(test(json_data['data'][1]['context']))
print(len(test(json_data['data'][1]['context'])))
