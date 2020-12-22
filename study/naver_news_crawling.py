import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import re
import csv


url = 'https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98%2019&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=35&start=1&refresh_start=0'
driver = webdriver.Chrome('C:\chromedriver')
driver.get(url=url)
time.sleep(3)
## 옵션 클릭
driver.find_element_by_xpath('//*[@id="search_option_button"]').click()
driver.find_element_by_xpath('//*[@id="snb"]/div/ul/li[5]/a').click()
driver.find_element_by_xpath('//*[@id="ca_1028"]').click()
driver.find_element_by_xpath('//*[@id="snb"]/div/ul/li[5]/div/span/span[1]/button').click()

title_list=[]
article=[]
for i in range(1,7):
    driver.find_element_by_xpath(f'//*[@id="main_pack"]/div[3]/div/div/a[{i}]').click()

    time.sleep(1)
    req = driver.page_source
    soup = BeautifulSoup(req,'html.parser')

    ##title뽑아내기, link 뽑아내기
    link_list = []
    links = soup.find_all(attrs={'class':'news_tit'})
    for text in links:
        title_list.append(text.attrs['title'])
    for a in links:
        link_list.append(a.attrs['href'])
        
    #article뽑아내기
    for link in link_list:
        webpage = requests.get(link,headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(webpage.content,'html.parser',from_encoding='utf-8')
        text = str(soup.find_all(attrs={'class':'text'}))
        article.append(re.sub('<.+?>','',text,0).strip().replace('\n','')[2:-27])
        time.sleep(1)
n=0
while n<1000:
    driver.find_element_by_xpath(f'//*[@id="main_pack"]/div[3]/div/div/a[6]').click()

    time.sleep(1)
    req = driver.page_source
    soup = BeautifulSoup(req,'html.parser')

    ##title뽑아내기, link 뽑아내기
    link_list = []
    links = soup.find_all(attrs={'class':'news_tit'})
    for text in links:
        title_list.append(text.attrs['title'])
    for a in links:
        link_list.append(a.attrs['href'])
        
    #article뽑아내기
    for link in link_list:
        webpage = requests.get(link,headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(webpage.content,'html.parser',from_encoding='utf-8')
        text = str(soup.find_all(attrs={'class':'text'}))
        article.append(re.sub('<.+?>','',text,0).strip().replace('\n','')[2:-27])
        time.sleep(1)
    n+=1

rows = zip(title_list,article)
with open('naver_news_covid19.csv','w',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['title','paragraphs'])
    for row in rows:
        writer.writerow(row)
