from urllib import request
from urllib import parse
import csv
# import wget

# url='http://15.165.152.90:8887/logpresso/httpexport/query.csv?_apikey=9867122c-d198-00ec-3195-006584f93e93&_q=proc+aihub_data(5000,1000)'
'''
import urllib2
try:
    response = urllib2.urlopen(url,timeout=5)
    content = response.read()
    f = open('local/index.csv',w')
    f.write(content)
    f.close()
    break
except urllib2.URLError as e:
    print(type(2))
'''
fname='./Q_A_dataset.csv'
import requests
import json
for i in range(1,10000,1000):
    data = f'_apikey=9867122c-d198-00ec-3195-006584f93e93&_q=proc+aihub_data({i},1000)'
    url = 'http://15.165.152.90:8887/logpresso/httpexport/query.csv?' + data
    r = requests.get(url)
# import pandas as pd
# print(r.content)
    with open(fname,'ab') as f:
        f.write(r.content)
# import json
# d = []
# rows = r.content.decode().split('\n')
# print(rows[0])
# from ast import literal_eval
# for row in rows:
#     d.append(literal_eval(row))
# print(d[:10])
# p = pd.DataFrame(j)
