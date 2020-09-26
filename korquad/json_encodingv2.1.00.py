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
    print(json_data['data'][1]['title'])
    print('=======================================')
    print(json_data['data'][1]['url'])
    print('=======================================')
    print(json_data['data'][1]['raw_html'])
    print('=======================================')
    print(json_data['data'][1]['qas'])