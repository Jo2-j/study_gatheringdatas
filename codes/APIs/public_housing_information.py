# - refer : https://www.data.go.kr/data/15058476/openapi.do
# - LH공사에서 관리하는 공공임대주택의 단지 정보 제공 수집
# - 지역 : 시도 이하 적용
# - 한국도로교통공단_자전거 교통사고 다발지역 정보 수집
# - 지역 : 시도 이하 적용



# 자전거 사고 데이터 api

# import requests

# url = f'http://apis.data.go.kr/B552061/frequentzoneBicycle/getRestFrequentzoneBicycle'

# byeonsu = {'serviceKey' : 'stCwIy%2BLoSZpTsxJ4usyyYV3yWNUePAIHISVLlDaFUMfDQDW77n8maQ0pmOH4aJy25qsGso7nLjNXokXaJDGlQ%3D%3D',
#             'searchYearCd' : '2021&siDo=11', 'guGun' : '110', 'type' : 'xml',
#             'numOfRows' : '10', 'pageNo' : '1'}

# response = requests.get(url, params=byeonsu)

# from bs4 import BeautifulSoup

# if response.status_code == 200: #200코드가 정상이라는 코드이므로 즉, 만약 정상이라고 판명되면~

#     mix = BeautifulSoup(response.text, 'xml') # soup처럼 모든 데이터를 믹스해놓은거, 여기서 xml이 하는 역할은 무엇인가
#     print(mix.prettify()) # 모든 데이터를 믹스해놓은거를 보기 좋게 이쁘게 바꾸자~
#     print('---')
#     return_auth_msg = mix.find('returnAuthMsg') # 만약  SERVICE_KEY_IS_NOT_REGISTERED_ERROR 관련 키가 나온다면? 그러니까 즉 값이 없는게 들어간다면
#     if return_auth_msg != None:
#         print(response.text) # 만약 관련 데이터가 없으면 정상이니까 그대로 인쇄
#     else:
#         print(f'return_auth_msg : {return_auth_msg}') # 만약에 데이터가 있다면 그 에러 메세지가 그대로 나오게끔
#     pass

from pymongo import MongoClient
import json
import requests


juso = input("서울에서 찾으려는 지역구(e.g. 강남구)")

print('-----')

def vehicleAccident(juso):
#https://apis.data.go.kr/B552061/frequentzoneBicycle/getRestFrequentzoneBicycle
#serviceKey=stCwIy%2BLoSZpTsxJ4usyyYV3yWNUePAIHISVLlDaFUMfDQDW77n8maQ0pmOH4aJy25qsGso7nLjNXokXaJDGlQ%3D%3D
# &searchYearCd=2021
#siDo=11
#guGun=110
#type=json
#numOfRows=10
#pageNo=1
    url = f'http://apis.data.go.kr/B552061/frequentzoneBicycle/getRestFrequentzoneBicycle?serviceKey=stCwIy%2BLoSZpTsxJ4usyyYV3yWNUePAIHISVLlDaFUMfDQDW77n8maQ0pmOH4aJy25qsGso7nLjNXokXaJDGlQ%3D%3D&searchYearCd=2021&siDo=11&guGun={juso}&type=json&numOfRows=10&pageNo=1'


    byeonsu = {'serviceKey' : 'stCwIy%2BLoSZpTsxJ4usyyYV3yWNUePAIHISVLlDaFUMfDQDW77n8maQ0pmOH4aJy25qsGso7nLjNXokXaJDGlQ%3D%3D',
            'searchYearCd' : '2021',  
            'siDo' : '11', 'guGun' : '110', 'type' : 'json',
            'numOfRows' : '10', 'pageNo' : '1'}
    
    # response = requests.get(url, params=byeonsu)
    response = requests.get(url)

    if response.status_code == 200:
        if response.text != '[]': # 값이 정상적으로 들어갔다면~
            content = json.loads(response.content)
            mongoClient = MongoClient('127.0.0.1:27017') # ""이든 ''이든 상관없나? 파이썬이라?
            database = mongoClient["study_accident"]
            collection = database["vehicleAccident"]
            result = collection.insert_many(content) # 매니는 딕셔너리, DB는 키 밸류값으로 들어가니까?
            pass
            return 

if __name__ == '__main__':
    vehicleAccident(juso)
    pass
