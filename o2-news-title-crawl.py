# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import random

# def google_news_titles_crawler(keyword, num_pages=2):
#     """
#     구글 뉴스에서 특정 키워드로 검색하여 뉴스 제목만 크롤링하는 함수
    
#     Parameters:
#     - keyword: 검색할 키워드
#     - num_pages: 크롤링할 페이지 수
    
#     Returns:
#     - titles_list: 수집된 뉴스 제목 리스트
#     """
#     titles_list = []
    
#     # User-Agent 설정 (구글 크롤링 방지 우회)
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#         'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
#     }
    
#     for page in range(0, num_pages*10, 10):
#         # 구글 뉴스 URL (검색어와 페이지 설정)
#         url = f"https://www.google.com/search?q={keyword}&tbm=nws&hl=ko&start={page}"
        
#         try:
#             # 요청 보내기
#             response = requests.get(url, headers=headers)
#             if response.status_code != 200:
#                 print(f"페이지 요청 실패: 상태 코드 {response.status_code}")
#                 continue
                
#             # HTML 파싱
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # 모든 링크 요소에서 제목 찾기 (다양한 방법으로 시도)
#             print(f"\n=== {page//10 + 1}페이지 제목 추출 시작 ===")
            
#             # 방법 1: 표준 뉴스 제목 선택자
#             articles = soup.select('div.SoaBEf')
#             if articles:
#                 print(f"방법 1로 {len(articles)}개 뉴스 블록 발견")
#                 for article in articles:
#                     # 여러 가능한 제목 선택자 시도
#                     title = None
                    
#                     # 방법 1-1: 일반적인 제목 태그
#                     for selector in ['h3', 'h4', 'div.mCBkyc', 'a[href*="url"]']:
#                         if title_elem := article.select_one(selector):
#                             if title_text := title_elem.get_text(strip=True):
#                                 title = title_text
#                                 break
                    
#                     # 제목을 찾았으면 추가
#                     if title and len(title) > 5 and title not in titles_list:
#                         titles_list.append(title)
#                         print(f"제목 추출 성공: {title[:40]}...")
            
#             # 방법 2: 다른 뉴스 컨테이너 시도
#             if len(titles_list) < (page//10 + 1) * 3:  # 충분한 제목을 찾지 못했다면
#                 for selector in ['g-card', 'div.xuvV6b', 'article', 'div.v7W49e']:
#                     articles = soup.select(selector)
#                     if articles:
#                         print(f"방법 2 ({selector})로 {len(articles)}개 뉴스 블록 발견")
#                         for article in articles:
#                             # 텍스트가 있는 모든 헤더 요소 찾기
#                             headers = article.select('h1, h2, h3, h4, h5, div[role="heading"]')
#                             for header in headers:
#                                 if title_text := header.get_text(strip=True):
#                                     if len(title_text) > 10 and title_text not in titles_list:
#                                         titles_list.append(title_text)
#                                         print(f"제목 추출 성공: {title_text[:40]}...")
            
#             # 방법 3: 마지막 시도 - 특정 클래스를 가진 요소 직접 검색
#             if len(titles_list) < (page//10 + 1) * 3:  # 여전히 충분한 제목을 찾지 못했다면
#                 print("방법 3: 클래스 기반 검색")
#                 for class_name in ['mCBkyc', 'DY5T1d', 'vJOb1e', 'RD0gLb', 'n0jPhd']:
#                     title_elems = soup.select(f'.{class_name}')
#                     for elem in title_elems:
#                         if title_text := elem.get_text(strip=True):
#                             if len(title_text) > 10 and title_text not in titles_list:
#                                 titles_list.append(title_text)
#                                 print(f"제목 추출 성공: {title_text[:40]}...")
            
#             # 방법 4: 모든 링크 텍스트에서 긴 텍스트를 제목으로 간주
#             if len(titles_list) < (page//10 + 1) * 2:  # 여전히 제목을 별로 찾지 못했다면
#                 print("방법 4: 링크 텍스트 검색")
#                 all_links = soup.select('a')
#                 for link in all_links:
#                     if link_text := link.get_text(strip=True):
#                         if len(link_text) > 20 and link_text not in titles_list:
#                             titles_list.append(link_text)
#                             print(f"제목 추출 성공: {link_text[:40]}...")
                            
#                             # 충분한 수의 제목을 찾았다면 중단
#                             if len(titles_list) >= (page//10 + 1) * 5:
#                                 break
            
#             print(f"현재까지 추출된 제목 수: {len(titles_list)}")
                
#             # 구글 차단 방지를 위한 랜덤 지연
#             delay = random.uniform(1.5, 3.0)
#             print(f"{delay:.1f}초 대기...")
#             time.sleep(delay)
            
#         except Exception as e:
#             print(f"페이지 처리 중 오류 발생: {e}")
#             continue
    
#     return titles_list

# # 실행
# keyword = "오투저축은행"
# print(f"'{keyword}' 키워드로 뉴스 제목 크롤링 시작...")
# titles = google_news_titles_crawler(keyword, num_pages=1)

# # 결과 확인
# print("\n===== 수집 결과 =====")
# print(f"수집된 뉴스 제목 수: {len(titles)}")
# for i, title in enumerate(titles, 2):
#     if i <= 1000:  # 처음 10개만 출력
#         print(f"{i}. {title}")
#     else:
#         print(f"... 외 {len(titles) - 10}개")
#         break

# # 결과를 데이터프레임으로 변환하고 CSV 파일로 저장
# if titles:
#     df = pd.DataFrame(titles, columns=['title'])
#     file_name = f"{keyword}_news_titles.csv"
#     df.to_csv(file_name, index=False, encoding='utf-8-sig')
#     print(f"\n결과가 {file_name} 파일에 저장되었습니다.")

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from datetime import datetime, timedelta

def google_news_title_date_crawler(keyword, num_pages=3):
    """
    구글 뉴스에서 특정 키워드로 검색하여 뉴스 제목과 날짜를 크롤링하는 함수
    
    Parameters:
    - keyword: 검색할 키워드
    - num_pages: 크롤링할 페이지 수
    
    Returns:
    - news_data: 수집된 뉴스 제목과 날짜 정보 딕셔너리 리스트
    """
    news_data = []
    
    # User-Agent 설정 (구글 크롤링 방지 우회)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    for page in range(0, num_pages*10, 10):
        # 구글 뉴스 URL (검색어와 페이지 설정)
        url = f"https://www.google.com/search?q={keyword}&tbm=nws&hl=ko&start={page}"
        
        try:
            # 요청 보내기
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"페이지 요청 실패: 상태 코드 {response.status_code}")
                continue
                
            # HTML 파싱
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 뉴스 블록 찾기
            print(f"\n=== {page//10 + 1}페이지 뉴스 추출 시작 ===")
            
            # 방법 1: 일반적인 뉴스 컨테이너 선택자
            articles = soup.select('div.SoaBEf')
            if articles:
                print(f"{len(articles)}개 뉴스 블록 발견")
                for article in articles:
                    news_item = {}
                    
                    # 제목 추출 시도 (여러 가능한 위치)
                    title_elem = None
                    for selector in ['div.n0jPhd', 'div.mCBkyc', 'h3', 'h4', 'a[href*="url"]']:
                        if title_elem := article.select_one(selector):
                            title_text = title_elem.get_text(strip=True)
                            if title_text and len(title_text) > 5:
                                news_item['title'] = title_text
                                break
                    
                    # 날짜 추출 시도 (여러 가능한 위치)
                    date_elem = None
                    for selector in ['span.WG9SHc', 'div.OSrXXb', 'span.sZLk0b', 'div.wxp1Sb']:
                        if date_elem := article.select_one(selector):
                            date_text = date_elem.get_text(strip=True)
                            if date_text:
                                news_item['date'] = date_text
                                break
                    
                    if 'title' in news_item:
                        # 날짜 정보가 없으면 "날짜 정보 없음"으로 설정
                        if 'date' not in news_item:
                            news_item['date'] = "날짜 정보 없음"
                        
                        # 중복 확인
                        if not any(item.get('title') == news_item['title'] for item in news_data):
                            news_data.append(news_item)
                            print(f"뉴스 추출: {news_item['title'][:40]}... | {news_item['date']}")
            
            # 대체 방법: 다른 클래스 구조의 뉴스 컨테이너 시도
            if len(news_data) < (page//10 + 1) * 5:  # 충분한 뉴스를 찾지 못했다면
                print("대체 방법 시도...")
                
                # 뉴스 제목이 있을 수 있는 요소들 검색
                title_elements = soup.select('h3.LC20lb, div.mCBkyc, div.n0jPhd, div.vJOb1e')
                for title_elem in title_elements:
                    if title_elem.parent and title_elem.parent.parent:  # 상위 요소가 있어야 뉴스 항목일 가능성이 높음
                        news_item = {}
                        title_text = title_elem.get_text(strip=True)
                        
                        if len(title_text) > 10:  # 짧은 텍스트는 제외
                            news_item['title'] = title_text
                            
                            # 같은 컨테이너 안에서 날짜 정보 찾기 (상위 3단계까지 탐색)
                            container = title_elem.parent.parent
                            date_elem = None
                            
                            # 현재 요소와 주변에서 날짜 정보 검색
                            date_candidates = container.select('span.WG9SHc, span.sZLk0b, div.wxp1Sb, div.OSrXXb')
                            if date_candidates:
                                date_text = date_candidates[0].get_text(strip=True)
                                news_item['date'] = date_text
                            else:
                                news_item['date'] = "날짜 정보 없음"
                            
                            # 중복 확인
                            if 'title' in news_item and not any(item.get('title') == news_item['title'] for item in news_data):
                                news_data.append(news_item)
                                print(f"뉴스 추출(대체): {news_item['title'][:40]}... | {news_item['date']}")
            
            print(f"현재까지 추출된 뉴스 수: {len(news_data)}")
                
            # 구글 차단 방지를 위한 랜덤 지연
            delay = random.uniform(1.5, 3.0)
            print(f"{delay:.1f}초 대기...")
            time.sleep(delay)
            
        except Exception as e:
            print(f"페이지 처리 중 오류 발생: {str(e)}")
            continue
    
    return news_data

def collect_news_over_years(keyword, years=3, pages_per_period=2):
    """
    여러 해에 걸쳐 뉴스를 수집하는 함수
    
    Parameters:
    - keyword: 검색할 키워드
    - years: 수집할 연도 수
    - pages_per_period: 각 기간마다 크롤링할 페이지 수
    
    Returns:
    - all_news_data: 수집된 모든 뉴스 데이터
    """
    all_news_data = []
    
    # User-Agent 설정 (구글 크롤링 방지 우회)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    # 현재 날짜
    end_date = datetime.now()
    
    # 3개월 간격으로 나눠서 수집
    for i in range(years * 4):
        # 시작일과 종료일 설정 (3개월 간격)
        end_of_period = end_date - timedelta(days=i*90)
        start_of_period = end_of_period - timedelta(days=90)
        
        # 날짜 형식 변환 (YYYY/MM/DD)
        start_date_str = start_of_period.strftime('%Y/%m/%d')
        end_date_str = end_of_period.strftime('%Y/%m/%d')
        
        print(f"\n===== 수집 기간: {start_date_str} ~ {end_date_str} =====")
        period_news_data = []
        
        for page in range(0, pages_per_period*10, 10):
            # tbs=cdr:1,cd_min:{시작일},cd_max:{종료일} 파라미터로 날짜 범위 지정
            url = f"https://www.google.com/search?q={keyword}&tbm=nws&hl=ko&tbs=cdr:1,cd_min:{start_date_str},cd_max:{end_date_str}&start={page}"
            
            try:
                # 요청 보내기
                response = requests.get(url, headers=headers)
                if response.status_code != 200:
                    print(f"페이지 요청 실패: 상태 코드 {response.status_code}")
                    continue
                    
                # HTML 파싱
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 뉴스 블록 찾기
                print(f"\n=== 기간: {start_date_str}~{end_date_str}, {page//10 + 1}페이지 뉴스 추출 시작 ===")
                
                # 방법 1: 일반적인 뉴스 컨테이너 선택자
                articles = soup.select('div.SoaBEf')
                if articles:
                    print(f"{len(articles)}개 뉴스 블록 발견")
                    for article in articles:
                        news_item = {}
                        
                        # 제목 추출 시도 (여러 가능한 위치)
                        title_elem = None
                        for selector in ['div.n0jPhd', 'div.mCBkyc', 'h3', 'h4', 'a[href*="url"]']:
                            if title_elem := article.select_one(selector):
                                title_text = title_elem.get_text(strip=True)
                                if title_text and len(title_text) > 5:
                                    news_item['title'] = title_text
                                    break
                        
                        # 날짜 추출 시도 (여러 가능한 위치)
                        date_elem = None
                        for selector in ['span.WG9SHc', 'div.OSrXXb', 'span.sZLk0b', 'div.wxp1Sb']:
                            if date_elem := article.select_one(selector):
                                date_text = date_elem.get_text(strip=True)
                                if date_text:
                                    news_item['date'] = date_text
                                    break
                        
                        if 'title' in news_item:
                            # 날짜 정보가 없으면 "날짜 정보 없음"으로 설정
                            if 'date' not in news_item:
                                news_item['date'] = "날짜 정보 없음"
                            
                            # 수집 기간 정보 추가
                            news_item['period'] = f"{start_date_str}~{end_date_str}"
                            
                            # 중복 확인 (전체 데이터에서 확인)
                            if not any(item.get('title') == news_item['title'] for item in all_news_data):
                                period_news_data.append(news_item)
                                all_news_data.append(news_item)
                                print(f"뉴스 추출: {news_item['title'][:40]}... | {news_item['date']}")
                
                # 대체 방법: 다른 클래스 구조의 뉴스 컨테이너 시도
                if len(period_news_data) < (page//10 + 1) * 5:  # 충분한 뉴스를 찾지 못했다면
                    print("대체 방법 시도...")
                    
                    # 뉴스 제목이 있을 수 있는 요소들 검색
                    title_elements = soup.select('h3.LC20lb, div.mCBkyc, div.n0jPhd, div.vJOb1e')
                    for title_elem in title_elements:
                        if title_elem.parent and title_elem.parent.parent:  # 상위 요소가 있어야 뉴스 항목일 가능성이 높음
                            news_item = {}
                            title_text = title_elem.get_text(strip=True)
                            
                            if len(title_text) > 10:  # 짧은 텍스트는 제외
                                news_item['title'] = title_text
                                
                                # 같은 컨테이너 안에서 날짜 정보 찾기 (상위 3단계까지 탐색)
                                container = title_elem.parent.parent
                                date_elem = None
                                
                                # 현재 요소와 주변에서 날짜 정보 검색
                                date_candidates = container.select('span.WG9SHc, span.sZLk0b, div.wxp1Sb, div.OSrXXb')
                                if date_candidates:
                                    date_text = date_candidates[0].get_text(strip=True)
                                    news_item['date'] = date_text
                                else:
                                    news_item['date'] = "날짜 정보 없음"
                                
                                # 수집 기간 정보 추가
                                news_item['period'] = f"{start_date_str}~{end_date_str}"
                                
                                # 중복 확인 (전체 데이터에서 확인)
                                if 'title' in news_item and not any(item.get('title') == news_item['title'] for item in all_news_data):
                                    period_news_data.append(news_item)
                                    all_news_data.append(news_item)
                                    print(f"뉴스 추출(대체): {news_item['title'][:40]}... | {news_item['date']}")
                
                print(f"현재 기간 추출된 뉴스 수: {len(period_news_data)} / 총 누적 뉴스 수: {len(all_news_data)}")
                    
                # 구글 차단 방지를 위한 랜덤 지연 (페이지 간)
                delay = random.uniform(1.5, 3.0)
                print(f"{delay:.1f}초 대기...")
                time.sleep(delay)
                
            except Exception as e:
                print(f"페이지 처리 중 오류 발생: {str(e)}")
                continue
        
        # 기간별 수집 결과 출력
        print(f"\n=== {start_date_str}~{end_date_str} 기간 수집 완료: {len(period_news_data)}개 ===")
        
        # 구글 차단 방지를 위한 랜덤 지연 (기간 사이)
        delay = random.uniform(3.0, 5.0)
        print(f"{delay:.1f}초 대기...")
        time.sleep(delay)
    
    return all_news_data

# 실행 코드
if __name__ == "__main__":
    keyword = "저축은행"
    print(f"'{keyword}' 키워드로 뉴스 제목과 날짜 크롤링 시작...")
    
    # 방법 1: 단순히 페이지 수를 늘려 최근 뉴스 더 많이 가져오기
    news_items = google_news_title_date_crawler(keyword, num_pages=1000)
    
    # 방법 2: 3년치 데이터 수집 (특정 기간별로 나눠서 수집)
    # news_items = collect_news_over_years(keyword, years=3, pages_per_period=2)
    
    # 결과 확인
    print("\n===== 수집 결과 =====")
    print(f"수집된 뉴스 수: {len(news_items)}")
    for i, item in enumerate(news_items, 1):
        if i <= 10:  # 처음 10개만 출력
            print(f"{i}. {item['title']} | {item['date']}")
        elif i == 11:
            print(f"... 외 {len(news_items) - 10}개")
            break

    # 결과를 데이터프레임으로 변환하고 CSV 파일로 저장
    if news_items:
        df = pd.DataFrame(news_items)
        file_name = f"{keyword}_news_with_dates.csv"
        df.to_csv(file_name, index=False, encoding='utf-8-sig')
        print(f"\n결과가 {file_name} 파일에 저장되었습니다.")
        
        # 데이터프레임 확인
        print("\n데이터프레임 미리보기:")
        print(df.head())
