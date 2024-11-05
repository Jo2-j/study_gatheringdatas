import requests
import json

def main():
    uri = f'https://openapi.naver.com/v1/search/blog'
    params = {'query' : '진주'} # 딕셔너리 형식으로 들어가야 하니까
    headers = {'X-Naver-Client-Id' : 'OY_jNcne5A0AmQF1OMHi' , 'X-Naver-Client-Secret' : 'q_0GyJqVpU'} # 역시 딕셔너리 형식으로 들어가니까
    response = requests.get(url=uri, params=params, headers=headers) # like postman
    
    if response.status_code == 200: # status_code는 변수이므로 비교만 가능함, 또 함수는 행동을 하는거지만 비교도 가능 비교를 할때는, 가지고 나온 데이터값이랑 비교를함 
        contents = json.loads(response.text)    # python에서 다루기 편하게
        pass
    return
if __name__ == '__main__':
    main()
    pass
