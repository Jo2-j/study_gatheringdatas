# 이미지 다운로드
# refer : http://www.cgv.co.kr/movies/?lt=1&ft=0
# target : div.box-image > a > span > img

# 사진 가져오기
# src만 가져와서 download

import requests

response = requests.get('http://www.cgv.co.kr/movies/?lt=1&ft=0') # 끌고 내려올때

from bs4 import BeautifulSoup # 수프만들때, 재료 가져와서 요리하는거

#html을 구조화(=  함수로 만든다, 여러번 할때 틀을 만들어 놓음) class 목적이 있는 집합체
soup = BeautifulSoup(response.text, 'html.parser')
image_link_list = soup.select('div.box-image > a > span > img')
# for in [[class는 기성품화 된 밥솥 왜냐 밥을 잘 지으라고 만들어 놓은 걸 사용함, function은 기능 즉 행동하는 애임, 
# temp_list = list() 처럼 복제하는
# 틀이 있는애를 찍어낸다]] .은 상위 하위 를 나타내는것 상위.하위 
# #하지만 function이 행동할때 상위 개념인 class를 뱉어낼수도 있다는 사실을 명심하자 드라이버로 부품을 만들 수 있기에
# class라는 걸 기계라고 생각해보자 



#저장 위치 정하기
import os
folder_name = f'./downloads'
if not os.path.exists(folder_name): # 있으면 지나가고, 없으면 만들고
    os.mkdir(folder_name)

import urllib.request as req

for index, image_link in enumerate(image_link_list): # 이미지 링크 리스트를 푼다 라고 생각하자, enumerate는 인식표 붙여줄때
    image_url = image_link.attrs['src'] # 이미지 링크에 attrs(고르는거)를 사용하여 src만 빼내온다 attrs는 tag라는 class 의 변수
    # attrs라는 function(기능)을 타입을 찍어보면 dic로 나온다 즉, dic에 맞는 []로 쓴다
    req.urlretrieve(image_url, f'{folder_name}/{index}.jpg')
    pass


# def main():
#     respone = requests.get(f'http://www.cgv.co.kr/movies/?lt=1&ft=0')
#     soup = BeautifulSoup(respone.text, 'html.parser')
#     news_list = soup.select('div.col-inner')
    
#     for news in news_list:
#         title_link = news.select_one('h1.title > a')
#         print(title_link.text)
#         print(f'link : {title_link.attrs['href']}')
#         print(f'date : {date.text}')
#         pass
    
    
    
#     return



# if __name__ == '__main__':
#     main()
#     pass