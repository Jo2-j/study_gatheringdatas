# 링크, 제목, 날짜 묶음 가져오기

# div.col-inner
# 제목, 링크 : h1.title > a
# 날짜 : div.new_info > span.time > span


import requests

from bs4 import BeautifulSoup

def main():
    respone = requests.get(f'https://underkg.co.kr/news')
    soup = BeautifulSoup(respone.text, 'html.parser')
    news_list = soup.select('div.col-inner')
    
    for news in news_list:
        title_link = news.select_one('h1.title > a')
        print(title_link.text)
        print(f'link : {title_link.attrs['href']}')
        print(f'date : {date.text}')
        pass
    
    
    
    return



if __name__ == '__main__':
    main()
    pass