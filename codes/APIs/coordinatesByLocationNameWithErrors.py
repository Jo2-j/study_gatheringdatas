# Python3 샘플 코드 #

import requests

url = 'https://api.openweathermap.org/data/2.5/weather?lat=34.0901&lon=-118.4065&appid=625ad48b4201c59ee5b4e548892fcb40'
params ={'city' : 'tokyo',
         'country' : 'guam', 'country' : 'monaco', 
        'appid' : '625ad48b4201c59ee5b4e548892fcb40'}

response = requests.get(url, params=params)

if response.status_code == 200:
        if response.text != '[]':      
                # print(response.content)

                import json
                content = json.loads(response.content)


                # mongoDB 저장
                from pymongo import MongoClient
                # mongodb에 접속 -> 자원에 대한 class
                mongoClient = MongoClient("python_selenium_drive_mongo-db_mongodb_7-1")
                # database 연결
                database = mongoClient["study_finance"]
                # collection 작업
                collection = database['coordinatesByLocationOnName']

                result = collection.insert_many(content)
                pass
        else : 
                print(f'result empty : {response.text}')
else:
        print(f'error : {response.status_code}')