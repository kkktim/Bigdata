"""
    날짜 : 2022/03/07
    이름 : 강태호
    내용 : MongoDB find 실습
"""
from pymongo import MongoClient as mongo
from datetime import datetime

#1단계 - MongoDB 접속
conn = mongo('mongodb://timk:1234@192.168.56.101:27017')

#2단계 - DB 선택
db = conn.get_database('test')

#3단계 - Collection 선택
collection = db.get_collection('Member')

#4단계 - 쿼리실행
rs = collection.find()
for row in rs:
    print('{}, {}, {}, {}, {}, {}'.format(row['uid'], row['name'], row['hp'], row['pos'], row['dep'], row['rdate']))

#5단계 - MongoDB 종료
conn.close()