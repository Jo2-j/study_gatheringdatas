# # underkg.co.kr 뉴스 정보 수집
# # refer : https://underkg.co.kr/news/
# # -리스트에서 링크와 제목 가져오기
# # #board_list  h1 > a

# # -기사내용 확인 url
# # [href]

# # -기사내용
# # div.docInner > div.read_body


# import requests
# from bs4 import BeautifulSoup
# def main():
#     response = requests.get(f'https://underkg.co.kr/news/')
#     soup = BeautifulSoup(response.text, 'html.parser')
#     titles_link = soup.select('#board_list h1 > a')
#     for title_link in titles_link:
#         print(f'title : {title_link.text}')
#         news_content_url = title_link.attrs['href'] # 딕셔너리는 key, value 값으로 이루어 져있으며 싱글 싸줘야함 ''
#         print(f'news_content_url : {news_content_url}')
        
#         # 기사 내용 가져오기
#         response_content = requests.get(f'{news_content_url}') # {} 쓰는 이유는 변수 인식으로 하기 위함임
#         soup_content = BeautifulSoup(response_content.text, 'html.parser') # 콘텐츠는 결국 text이기 때문에 .text를 써야함
#         soup_content.select_one(f'div.docInner > div.read_body')
#         content = soup_content.select_one(f'div.docInner > div.read_body')
#         print(f'content : {content.text}')
#         print(f'--'*10)
#         pass
#     return

# if __name__ == '__main__':
#     main()
#     pass


# - underkg.co.kr 있는 news 정보 수집
# refer : https://underkg.co.kr/news
# - 리스트에서 링크와 제목 가져오기
# #board_list h1 > a
# - 기사내용 확인 uri
# [href]
# - 기사 내용 가져오기
# div.docInner > div.read_body
import requests
from bs4 import BeautifulSoup
def main():
    respone = requests.get(f'https://underkg.co.kr/news')
    soup = BeautifulSoup(respone.text, 'html.parser')
    titles_link = soup.select('#board_list h1 > a')
    for title_link in titles_link:
        print(f'title : {title_link.text}')
        news_content_url = title_link.attrs['href']
        print(f'news_content_url : {news_content_url}')
        # 기사 내용 가져오기
        respone_content = requests.get(f'{news_content_url}')
        soup_content = BeautifulSoup(respone_content.text, 'html.parser')
        content = soup_content.select_one(f'div.docInner > div.read_body')
        print(f'content : {content.text}')
        print(f'--'*10)
        pass
    return
if __name__ == '__main__':
    main()
    pass