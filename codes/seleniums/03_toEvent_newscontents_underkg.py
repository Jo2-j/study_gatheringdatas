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

browser.get(f'https://underkg.co.kr/news')

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

from selenium.webdriver.common.by import By

# news_list_tag = f'div.sa_thumb._LAZY_LOADING_ERROR_HIDE > div > a'
news_list_tag = f'div > div.thumb-wrap > a'
news_list = browser.find_elements(by=By.CSS_SELECTOR, value=news_list_tag)

import time
url_list = []

for num, news in enumerate(news_list):
    target_link = news.get_attribute(f'href')
    print(target_link)
    url_list.append(target_link)
    
    
    pass

for index, url in enumerate(url_list):
    browser.get(url)
    time.sleep(1)
    browser.back()
    time.sleep(1)
    pass