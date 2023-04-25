import datetime
import sqlite3
import requests

from bs4 import beatifulSoup
import sqlite3
while true:
       connection = sqlite3.connect('sinoptik_DB.sl3', 15)
       cur = connection.cursor()
cur.execute("INSERT INTO first_table (city TEXT,data TEXT,time TEXT,temperature TEXT);")
cur.execute("UPDATE first_table SET name='Sam' WHERE rowid=1;")
connection.commit()
response=request.get ('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BF%D1%80%D0%B0%D0%B3%D0%B0/2023-04-22')
 soup = beatifulSoup(responcse.text,featureste='html.parsers')
 soup_list = soup.find_all('div'('class':'lSIde'))
 res = soup_list {0}.find_('b',['class' 'today-temp'])

print(res.text)
cur.execute(f"INSERT INTO firs VALUES ('Миргород','{datetime.datetime.today().date()}','{datetime.datetime.today().time()}','{res.text}');")

res = cur.fetchall()
connection.close ()
