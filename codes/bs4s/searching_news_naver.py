# # # -리스트에서 링크와 제목 가져오기
# # #_SECTION_HEADLINE_LIST_9zk7c div.sa_text

# # 링크
# # https://news.naver.com/section/101

# #newsct > div.section_latest > div > div.section_latest_article._CONTENT_LIST._PERSIST_META > div > ul > li

# # div.section_latest_article._CONTENT_LIST._PERSIST_META > div > ul> li

# # 기사제목

# # ._PERSIST_META > div > ul > li > div > div > div.sa_text > a > strong
# import requests
# from bs4 import BeautifulSoup

# def main():
#     respone = requests.get(f'https://news.naver.com/section/101')
#     soup = BeautifulSoup(respone.text, 'html.parser')
#     titles_link = soup.select('._PERSIST_META > div > ul > li > div > div > div.sa_text > a > strong')
#     
#   for title_link in titles_link:
#         print(f'title : {title_link.text}')
#         news_content_url = title_link.attrs['href']
#         print(f'news_content_url : {news_content_url}')
#         # 기사 내용 가져오기
#         respone_content = requests.get(f'{news_content_url}')
#         soup_content = BeautifulSoup(respone_content.text, 'html.parser')
#         content = soup_content.select(f'#dic_area')
#         print(f'content : {content.text}')
#         print(f'--'*10)
#         pass
#     return
# if __name__ == '__main__':
#     main()
#     pass

import requests
from bs4 import BeautifulSoup

def main():
    response = requests.get('https://news.naver.com/section/101')
    soup = BeautifulSoup(response.text, 'html.parser')
    titles_link = soup.select('._PERSIST_META > div > ul > li > div > div > div.sa_text > a')

    for title_link in titles_link:
        print(f'title: {title_link.text.strip()}')
        news_content_url = title_link.attrs['href']
        print(f'news_content_url: {news_content_url}')
    
        response_content = requests.get(news_content_url)
        soup_content = BeautifulSoup(response_content.text, 'html.parser')
        content = soup_content.select_one('#dic_area')
        
        if content:
            print(f'content: {content.text.strip()}')
        else:
            print('No content found')
        
        print('--' * 10)

if __name__ == '__main__':
    main()
