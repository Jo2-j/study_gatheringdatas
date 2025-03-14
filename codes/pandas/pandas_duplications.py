from pymongo import MongoClient

# MongoDB 서버에 연결 : Both connect in case local and remote
client = MongoClient('mongodb://python_selenium_drive_mongo-db_mongodb_7-1:27017/' )

# 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
db = client['mydatabase']

# 'users' 컬렉션 선택 find
collection_users = db['users_collecting']
users_source = collection_users.find({}) #{} where절과 같은 특정한 값을 찾기 위해 이거는 python이 아니라 monggoDB이고 그 값이 json 형식으로 나타나니까 파이썬에서 사용하는 dictionary랑은 상관없음

# 중복 처리
import pandas as pd
df_data = pd.DataFrame(list(users_source))
df_users_source = df_data.drop_duplicates(subset=['name']) # 우리가 보기에는 같아도, 01234처럼 index(PK같은) 경우가 있기에 subset과 같이 특정하는걸 지정해줘야함!

# users_target insert
collection_target = db['users_target']
collection_target.insert_many(df_users_source.to_dict('records'))

pass