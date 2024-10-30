# - 검색어 따른 상품 정보 전부 수집

# 해야하는 행동(class.function()) :
# 0. 홈페이지 접속 및, 관련 from, import, tag정의하기
# 1. 상품클릭
# 2. 상품명, 가격, 상품상세 정보 가져오고 저장
# 3. 뒤로가기
# 4. 해당 페이지 상품 끝까지 반복
# 5. 페이지 마지막 버튼만 누르기(다음페이지)
# 6. 계속 반복후
# 7. 마지막 페이지(버튼 없어질때)까지 반복 후 나오기
# - 항목 : 상품명: div.pd-widget1__info-box > h2 , 가격: section.pd-price strong , 상품상세: #m2root
# - github, remote mongo uri 공유


# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities


# div.main.innerContent > div.searchAreaWrap > div 검색어? 아니면 직접? 

browser.get("https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=할로윈")

html = browser.page_source
print(html)

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time
import requests

next_page_button = f'a.srchPaginationNext' # 페이지칸
nextpage = browser.find_elements(by=By.CSS_SELECTOR, value=next_page_button)

each_item = f'div.s-goods__thumbnail'

while True:

#..



