from pymongo import MongoClient
import json
import requests

# 가져 오고 싶은 데이터의 api



def WthDat(city):

    '''
    http://api.openweathermap.org/geo/1.0/direct?q=London,mo,gum&limit=5&appid={API key}
    '''
    url = 'https://api.openweathermap.org/geo/1.0/direct' 
    params ={'q' : city,
            'appid' : '625ad48b4201c59ee5b4e548892fcb40'} 
    
    response = requests.get(url, params=params) # params의 의미가 무엇인지 그리고 =로 왜 이렇게 적었는지

    if response.status_code == 200: # 정상 통과 코드가 200이니까, 정상통과 되었다는 가정아래
        if response.text != '[]': # 만약 값이 정상적으로 들어갔다면
            #print(response.content)
            content = json.loads(response.content)
            #mongodb에 접속 -> 자원에 대한 class
            #mongoClient = MongoClient("python_selenium_drive_mongo-db_mongodb_7-1")
            mongoClient = MongoClient("127.0.0.1:27017")
            # database 연결
            database = mongoClient["study_finance"]
            # collection 작업
            collection = database['coordinatesByLocationOnName']
            result = collection.insert_many(content)
            pass
            return LatANDLon(content[0]['lat'], content[0]['lon'])
                
        else:
            print(f'result empty : {response.text}')
            return None
    else:
        print(f'error : {response.status_code}')
        return None
 


def LatANDLon(lat,lon):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'lat' : lat, 'lon' : lon, 
              'appid' : '625ad48b4201c59ee5b4e548892fcb40'}
    response = requests.get(url, params=params)
    if response.status_code == 200: # 정상 통과 코드가 200이니까, 정상통과 되었다는 가정아래
        if response.text != '[]': # 만약 값이 정상적으로 들어갔다면
            #print(response.content)
            content = json.loads(response.content)
            #mongodb에 접속 -> 자원에 대한 class
            #mongoClient = MongoClient("python_selenium_drive_mongo-db_mongodb_7-1")
            mongoClient = MongoClient("127.0.0.1:27017")
            # database 연결
            database = mongoClient["study_finance"]
            # collection 작업
            collection = database['coordinatesByLocationOnName']
            result = collection.insert_one(content)
            pass
        else:
            print(f'result empty : {response.text}')
    else:
        print(f'error : {response.status_code}')
    return

if __name__ == '__main__':
   first_list = ['tokyo', 'monaco', 'gu']
   for temp in first_list:
        WthDat(temp)