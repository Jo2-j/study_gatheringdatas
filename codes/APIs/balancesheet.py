# response = requests.get(url, params=params)

# if response.status_code == 200:
#         if response.text != '[]':      
#                 # print(response.content)

#                 import json
#                 content = json.loads(response.content)

#                 print(content)

# - 대상 : https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md#%EC%87%BC%ED%95%91
# - 하나에 request 두 개 collection에 저장
# - 하나에 request /search/shop
# - 두 개 collection : search_shop_info, search_shop_list(id_relative)
# - option : 쇼핑인사이트  -> 사용 등록 추가 필요, 리스트만 저장

import requests
import json

def main():

    url = f'http://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2/getBs_V2'

    params = {'serviceKey' : 'stCwIy%2BLoSZpTsxJ4usyyYV3yWNUePAIHISVLlDaFUMfDQDW77n8maQ0pmOH4aJy25qsGso7nLjNXokXaJDGlQ%3D%3D',
                'pageNo' : '1', 
                'numOfRows' : '1', 
                'resultType' : 'json', 
                'crno' : '1301110006246', 
                'bizYear' : '2019'}

    # headersByeonsu = {'X-Naver-Client-Id' : 'OY_jNcne5A0AmQF1OMHi' , 
    #                'X-Naver-Client-Secret' : 'q_0GyJqVpU'}

    response = requests.get(url=url, params=params)

    if response.status_code == 200: # 값이 오류가 나지 않으면
            contents = json.loads(response.text) # loads라는 function의 의미를 잘 모르겠음 누구한테 설명하기 어려움
            pass
    return

if __name__ == '__main__':
    main()
    pass