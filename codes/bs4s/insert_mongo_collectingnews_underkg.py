import requests

from bs4 import BeautifulSoup

def main():
    response = requests.get(f'https://underkg.co.kr/news')
    soup = BeautifulSoup(response.text, 'html.parser')
    titles_link = soup.select('#board_list h1 > a')
    
    news_title = []
    # for title_link in titles_link:
        #  news_title.append()
    for title_link in titles_link:
        news_title.append(title_link.get_text())
    

'''
    news_content = []

    news_content_url = title_link.attrs['href'] # 뉴스의 실제 화면으로 들어가는 하이퍼링크를 걸어준것
        # print(f'news_content_url : {news_content_url}')
        # 기사 내용 가져오기
    response_content = requests.get(f'{news_content_url}') # 하이퍼링크를 클릭한것
    soup_content = BeautifulSoup(response_content.text, 'html.parser') # 텍스트만 뽑아낸것
    content = soup_content.select_one(f'div.docInner > div.read_body')
    
    for ctt in content:
        content.append(title_link.get_text())
    print(f'content : {content.text}')
    print(f'--'*10)
        pass
    return

if __name__ == '__main__':
     main()
     pass

# if __name__ == '__main__':
#     main()
#     pass '''

# from pymongo import MongoClient
# # MongoDB 서버에 연결 : Both connect in case local and remote
# collecting_data = MongoClient('mongodb://192.168.0.63:27017/')

# # 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
# db = collecting_data['underkg']

# # 'users' 컬렉션 선택 (없으면 자동 생성)
# collection = db['news']

# # 입력할 데이터
# user_data = {
#     'title': 'John Doe',
#     'age': 30,
#     'email': 'johndoe@example.com'
# }

# # 데이터 입력
# result = collection.insert_one(user_data)

# # 입력된 문서의 ID 출력
# print('Inserted user id:', result.inserted_id)