# 1. 밑으로 내리고
# 2. 관련 내용을 찾아서 수집하기
# 3. 그 내용을 clova에게 주어서 긍정 부정 확인후
# 4. twit 내용, 그리고 관련 신호들을 다시 DB에 넣기 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CDM
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.chrome.options import Options as chromeOptions

webdriver_manager_directory = CDM().install()

def stockTwits():
    browser = webdriver.Chrome(service=chromeService(webdriver_manager_directory)) # 이 부분 위로 각각의 라인들이 어떤 일을 하는지 알아볼 필요는 있겠다.

    capabilities = browser.capabilities

    browser.get("https://stocktwits.com/symbol/ELAB")
    
# div.StreamMessage_messageContentDefault__cHL1P.StreamMessage_messageContent__T_T27.pr-4.relative.pr-0 > div > div > div