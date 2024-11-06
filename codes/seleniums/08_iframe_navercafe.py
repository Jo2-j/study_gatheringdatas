# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

webdriver_manager_directory = ChromeDriverManager().install()


def main():
    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities

    # - 주소 입력(https://www.w3schools.com/)

    browser.get("https://cafe.naver.com/sbabellows")

    # div.board-list > div > a
    import time
    time.sleep(2)
    cafeList = browser.switch_to.frame("cafe_main")
    browser.find_elements(by=By.CSS_SELECTOR, value='div.board-list > div > a')

    for index, row in enumerate(cafeList): #enumerate로 받았기에 index
        print(f'title : {row.text}')
        pass
    return

if __name__ == '__main__':
    main()
    pass
