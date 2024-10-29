# - 수집 데이터 mongodb에 insert
# - 항목 : 제목, 날짜, 읽은 수
# - github, remote mongo url 공유

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient

# MongoDB 서버에 연결 : Both connect in case local and remote
client = MongoClient('mongodb://192.168.0.63:27017/') # 같은 주소에 갈거면 def 밖에 정해주고 쓰자 왜냐면 같은 곳으로 가니까

def insertDB(abcd): # 먼저 선언을 해야함, 왜냐하면 def를 먼저하고 해야지 아래의 것에서 올리기때문에, 아니 그렇게 어렵게 생각하기 어려우면 내가 왜 이거를 적었는지 확인해보자

    # 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
    db = client['joesDB']
    # 'users' 컬렉션 선택 (없으면 자동 생성)
    collection = db['underKgNews']

    DBresult = collection.insert_one(abcd) # insert_one과 many의 차이 또한 def는 그냥 선언이기에 안에 들어가는거는 위치를 나타내므로 아래 ()안에 있는 값이랑 같게 나와야함
    # 입력된 문서의 ID 출력
    print('Inserted user id:', DBresult.inserted_id)

# def insertDB_Many(abcd): 생각해보기.. one - 딕셔너리 > many는 one(딕셔너리)의 합 - 리스트

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

capa = browser.capabilities # 케파란? 뭐지?

browser.get("https://underkg.co.kr/news")

pass # 왜 패스를 하지?

html = browser.page_source
print(html)

from selenium.webdriver.common.by import By

# h1 > a : title

# #board_list > div > div : bundle

# span.readNum
news_list = browser.find_elements(by=By.CSS_SELECTOR, value='div.col-inner')


results = []

for index, element_bundle in enumerate(news_list):
    news_title_tag = f'h1 > a'
    news_date_tag = f'span.time > span'
    news_read_tag = f'span.readNum > span'
    news_title = element_bundle.find_element(By.CSS_SELECTOR, news_title_tag)
    news_date = element_bundle.find_element(By.CSS_SELECTOR, news_date_tag)
    news_read = element_bundle.find_element(By.CSS_SELECTOR, news_read_tag)
    indi_result = f'제목 : {news_title.text}, 발행일 : {news_date.text}, 읽은 수 : {news_read.text}'
    dic_result = {"title" : news_title.text, "date" : news_date.text, "read" : news_read.text}

    results.append(dic_result)
    print(results)
    insertDB(dic_result)
    pass


# 차이점 요약
# 메서드	사용 용도	입력 형식	반환 값
# insert_one	단일 문서 삽입	딕셔너리	삽입된 문서의 _id (단일 ID)
# insert_many	다중 문서 삽입	딕셔너리 리스트	삽입된 문서들의 _id 리스트
# dic_result는 딕셔너리, results는 리스트.. 그러면 dic은 one으로 ? results는 many ?