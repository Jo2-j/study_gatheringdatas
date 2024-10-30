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

# - 주소 입력(https://www.w3schools.com/)
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")

# 상품들 페이지 이동하며 정보 수집

# 1-12페이지

# #area_itemlist > div.paginate > div > strong

# #area_itemlist > div.paginate > div > a

# - stop 키워드

# #area_itemlist > div.paginate > div > a.btn_next


# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time
import requests

element_value = f'#area_itemlist > div.paginate > div > strong, #area_itemlist > div.paginate > div > a'
page_list = browser.find_elements(by=By.CSS_SELECTOR, value=element_value)

element_selector_detail = f'#ty_thmb_view div.mnemitem_thmb_v2 > a'



for index in range(1, len(page_list))[8:]:
    time.sleep(3)
    pagination_list = browser.find_elements(by=By.CSS_SELECTOR, value=element_value)
    
    pagination_tag = pagination_list[index]

    btn_next = pagination_tag.get_attribute('class')

    if btn_next == 'btn_next':
        break
    pagination_tag.click()

    time.sleep(2)
    # 상세 정보 수집
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    detail_list = soup.select(element_selector_detail)
    for detail in detail_list:
        detail_url = detail.attrs['href']
        detail_url = f'https://emart.ssg.com/item{detail_url}'
        response = requests.get(detail_url)
        pass
    pass
pass


