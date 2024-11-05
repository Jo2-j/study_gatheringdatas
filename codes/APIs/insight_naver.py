# - 대상 : https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md#%EC%87%BC%ED%95%91
# - 하나에 request 두 개 collection에 저장
# - 하나에 request /search/shop
# - 두 개 collection : search_shop_info, search_shop_list(id_relative)
# - option : 쇼핑인사이트  -> 사용 등록 추가 필요, 리스트만 저장

import requests
import json

def insightNaver():
    uri = f'https://openapi.naver.com/v1/search/shop.json'
    paramsByeonsu = {'query' : '빼빼로'} # 파라미터는 key랑 valu로 이루어져있음 > dict
    headersByeonsu = {'X-Naver-Client-Id' : 'OY_jNcne5A0AmQF1OMHi' , 
               'X-Naver-Client-Secret' : 'q_0GyJqVpU'}
    response = requests.get(url=uri, params=paramsByeonsu, headers=headersByeonsu)

    if response.status_code == 200: # 값이 오류가 나지 않으면
        contents = json.loads(response.text) # loads라는 function의 의미를 잘 모르겠음 누구한테 설명하기 어려움
        pass    
    return

if __name__ == '__main__':
    insightNaver()
    pass
