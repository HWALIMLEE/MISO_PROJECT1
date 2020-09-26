import json
from pprint import pprint
result=[]
with open('KorQuAD_v1.0_train.json','r',encoding='utf-8')as json_file:
    json_data = json.load(json_file)
    print(json_data.keys())
    print(len(json_data['data'])) #
    # print(json_data['data'][0]['paragraphs'])
    print(json_data['data'][1]['paragraphs'][0]['qas'][0]['answers'])