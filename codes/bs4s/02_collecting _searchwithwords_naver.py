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

titles = soup.select('span.lnk_tit')

for title in titles : 
    print(title.text)
    
# len(titles)
# 13
# titles[10]
# <span class="lnk_tit">300만원 대출 둥지대부에서</span>
# for title in titles : 
#     print(title.text)
# 당일 소액대출 전문 둥지대부
# 300만원까지 당일입금!
# 300만원 소액대출 위머니
# 비대면 무서류
# 급할수록 빠르게 위머니
# 실시간
# 소액대출 급전 전문
# 당일신청 당일입금 위머니대부
# 소득증빙 필요없이 위머니
# 걱정없이 지금바로 GO
# 300만원 대출 둥지대부에서
# 누구나 300만원! 위머니
# 당일 입금


pass
