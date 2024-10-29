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

# target : https://accounts.kakao.com/login/?continue=https%3A%2F%2Fwww.daum.net#login

# target tag(input) : #loginId--1

# target tag(input) : #password--2

# target tag(click) : #recaptcha-anchor > div.recaptcha-checkbox-border

# target tag(click) : button.btn_g.highlight.submit
# - 주소 입력(https://www.w3schools.com/)

browser.get("https://accounts.kakao.com/login/?continue=https%3A%2F%2Fwww.daum.net#login")

# - 가능 여부에 대한 OK 받음

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

from selenium.webdriver.common.by import By
element_value = f'#loginId--1'
element_id = browser.find_element(by=By.CSS_SELECTOR, value=element_value)
element_id.send_keys('w01205250623@nate.com')

element_value = f'#password--2'
element_pw = browser.find_element(by=By.CSS_SELECTOR, value=element_value)
element_pw.send_keys('')


try :
    element_value = f'#recaptcha-anchor > div.recaptcha-checkbox-border'
    element_isRobot = browser.find_element(by=By.CSS_SELECTOR, value=element_value)
    element_isRobot.click('')
except Exception as e:
    pass

element_value = f'button.btn_g.highlight.submit'
element_button = browser.find_element(by=By.CSS_SELECTOR, value=element_value)
element_button.click()

pass
