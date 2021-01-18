#  Inserting Pandas DataFrames Into Databases Using to_sql
import pandas as pd
import pymysql
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb

data = pd.read_csv(r'C:\Users\hwali\MISO_Project1\nlpqa\data\suwon_samsung.csv',encoding='utf-8')

engine = create_engine("mysql+mysqldb://root:"+"root"+"@localhost/suwon", encoding='utf-8')
conn = engine.connect()

data.to_sql(name='suwon_samsung',con=engine,if_exists='append',index=False)
conn.close()
