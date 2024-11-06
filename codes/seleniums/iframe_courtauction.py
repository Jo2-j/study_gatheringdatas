# 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager as CDM
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
webdriver_manager_directory = CDM().install()


def iframeCourtAuction():
    # chromeDriver 실행? 더 잘알아보자
    browser = webdriver.Chrome(service=chromeService(webdriver_manager_directory))
    # chromeWebDriver의 capa 속성 사용
    capabilities = browser.capabilities

    sendAddress = browser.get('https://www.courtauction.go.kr/') # 주소 전송하고, 비어 있는 아이프레임
    
    enterSite = browser.switch_to.frame("indexFrame") # 스위치는 켜주는거
    
    clickUrl = f'#main_btn' # 어떤걸 클릭할건데? 

    clickButton = browser.find_element(by=By.CSS_SELECTOR, value=clickUrl)
    
    clickButton.click()
    
    pass

if __name__ == '__main__':
    iframeCourtAuction()
    pass



'''/index.jsp 법원 경매 사이트에서는 검색 그니까 들어가고 싶은 홈페이지에 url을 직접 찾기 어려우면(iframe으로 쌓여있을때) 
내가 직접 어떻게 들어가는지 보고 클릭하는 그 순간을 포착하여서 거기서 (i)frame으로 태그되어있는걸 찾는다'''