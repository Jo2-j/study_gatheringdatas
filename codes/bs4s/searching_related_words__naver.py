# 0. 연관검색어

# 1. 연관검색어를 append로 추가

# 2. 리스트의 값을 하나하나 다시 써치

# 3. 그 관련된 값의 제목을 다시 gathering

# 4. gathering 된 값 바구니에 넣기


# Naver 지식인 검색어 따른 타이틀 수집

# span.lnk_tit

# Ref: https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B8%88%EC%9C%B5

import requests # url 주소 입력하고 해당 주소 입력과 해당 html을 가져오는 것 

# 검색어 받기

keyword = input('input search word : ')

# 브라우저 주소창

    
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}'
response = requests.get(url)

from bs4 import BeautifulSoup # html 해석기

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('div.faSBppRge_X6pwl2rZi4._CVSsJs5H34NvpNMMCIA')


for title in titles : 
    print(title.text)


pass
