# # # # from selenium import webdriver
# # # # from selenium.webdriver.common.by import By
# # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # from selenium.webdriver.support import expected_conditions as EC
# # # # from selenium.common.exceptions import TimeoutException, NoSuchElementException
# # # # from datetime import datetime
# # # # from selenium.webdriver.chrome.service import Service
# # # # from selenium.webdriver.chrome.options import Options
# # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # import pandas as pd
# # # # import time
# # # # import csv
# # # # import os

# # # # class NaverBlogCrawler:
# # # #     def __init__(self):
# # # #         # Chrome 옵션 설정
# # # #         self.options = Options()
# # # #         self.options.add_argument('--headless')  # 리눅스 환경에서 필수
# # # #         self.options.add_argument('--no-sandbox')
# # # #         self.options.add_argument('--disable-dev-shm-usage')
# # # #         self.options.add_argument('--disable-gpu')
# # # #         self.options.add_argument('--window-size=1920x1080')
# # # #         self.options.add_argument('--disable-notifications')
# # # #         self.options.add_argument('--remote-debugging-port=9222')
        
# # # #         try:
# # # #             # WebDriver 초기화 시도
# # # #             service = Service(ChromeDriverManager().install())
# # # #             self.driver = webdriver.Chrome(service=service, options=self.options)
# # # #         except Exception as e:
# # # #             print(f"기본 방식 초기화 실패: {e}")
# # # #             try:
# # # #                 # 직접 크롬드라이버 경로 지정 방식 시도
# # # #                 service = Service('/usr/bin/chromedriver')
# # # #                 self.driver = webdriver.Chrome(service=service, options=self.options)
# # # #             except Exception as e2:
# # # #                 print(f"대체 방식도 실패: {e2}")
# # # #                 raise

# # # #         self.wait = WebDriverWait(self.driver, 10)
# # # #         self.posts = []
        
# # # #     def create_csv(self, filename):
# # # #         if not os.path.exists(filename):
# # # #             with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
# # # #                 writer = csv.writer(f)
# # # #                 writer.writerow(['제목', '날짜', 'URL', '카테고리'])
    
# # # #     def save_to_csv(self, data, filename):
# # # #         with open(filename, 'a', newline='', encoding='utf-8-sig') as f:
# # # #             writer = csv.writer(f)
# # # #             writer.writerow(data)
    
# # # #     def is_target_month(self, date_str):
# # # #         try:
# # # #             date = datetime.strptime(date_str, '%Y. %m. %d.')
# # # #             if date.year == 2024 and date.month == 11:
# # # #                 return 'STOP'
# # # #             return date.year == 2024 and date.month in [12]
# # # #         except ValueError:
# # # #             return False

# # # #     def crawl_page(self, url):
# # # #         try:
# # # #             self.driver.get(url)
# # # #             time.sleep(2)
            
# # # #             posts = self.wait.until(EC.presence_of_all_elements_located(
# # # #                 (By.CSS_SELECTOR, '#PostThumbnailAlbumViewArea > ul > li')))
            
# # # #             for post in posts:
# # # #                 try:
# # # #                     title = post.find_element(By.CSS_SELECTOR, 'a > div.area_text').text.strip()
# # # #                     date = post.find_element(By.CSS_SELECTOR, 'a > div.area_text > span.date').text.strip()
                    
# # # #                     target_check = self.is_target_month(date)
# # # #                     if target_check == 'STOP':
# # # #                         print("2024년 11월 게시물 발견. 크롤링을 중단합니다.")
# # # #                         return False
                    
# # # #                     if target_check:
# # # #                         post_url = post.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
# # # #                         category = self.get_category_name(url)
                        
# # # #                         self.save_to_csv([title, date, post_url, category], 'naver_blog_posts.csv')
# # # #                         self.posts.append({
# # # #                             '제목': title,
# # # #                             '날짜': date,
# # # #                             'URL': post_url,
# # # #                             '카테고리': category
# # # #                         })
                        
# # # #                 except NoSuchElementException:
# # # #                     continue
                
# # # #             return True
            
# # # #         except Exception as e:
# # # #             print(f"페이지 크롤링 중 오류 발생: {e}")
# # # #             return False

# # # #     def get_category_name(self, url):
# # # #         category_map = {
# # # #             '58': '카테고리1',
# # # #             '56': '카테고리2',
# # # #             '10': '카테고리3'
# # # #         }
# # # #         for cat_num in category_map.keys():
# # # #             if f'categoryNo={cat_num}' in url:
# # # #                 return category_map[cat_num]
# # # #         return '기타'

# # # #     def crawl_all_pages(self, base_url):
# # # #         page = 1
# # # #         while True:
# # # #             url = f"{base_url}&currentPage={page}"
# # # #             print(f"현재 페이지 크롤링 중 {page}: {url}")
            
# # # #             if not self.crawl_page(url):
# # # #                 break
                
# # # #             try:
# # # #                 next_page = self.driver.find_element(
# # # #                     By.CSS_SELECTOR, 
# # # #                     'div.wrap_blog2_paginate > div > a:last-child'
# # # #                 )
# # # #                 if 'next' not in next_page.get_attribute('class'):
# # # #                     break
# # # #                 page += 1
# # # #                 time.sleep(1)
# # # #             except NoSuchElementException:
# # # #                 break

# # # #     def run(self):
# # # #         try:
# # # #             self.create_csv('naver_blog_posts.csv')
            
# # # #             urls = [
# # # #                 "https://blog.naver.com/PostList.naver?blogId=boryeongsi&from=postList&categoryNo=58",
# # # #                 "https://blog.naver.com/PostList.naver?blogId=boryeongsi&from=postList&categoryNo=56&parentCategoryNo=56",
# # # #                 "https://blog.naver.com/PostList.naver?blogId=boryeongsi&from=postList&categoryNo=10&parentCategoryNo=10"
# # # #             ]
            
# # # #             for url in urls:
# # # #                 print(f"카테고리 URL 크롤링 시작: {url}")
# # # #                 self.crawl_all_pages(url)
                
# # # #             if self.posts:
# # # #                 df = pd.DataFrame(self.posts)
# # # #                 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# # # #                 excel_filename = f'naver_blog_posts_{timestamp}.xlsx'
                
# # # #                 try:
# # # #                     df.to_excel(excel_filename, index=False)
# # # #                     print(f"데이터가 성공적으로 저장되었습니다: {excel_filename}")
# # # #                 except Exception as e:
# # # #                     print(f"Excel 파일 저장 중 오류 발생: {e}")
# # # #                     # CSV 형식으로 백업 저장
# # # #                     csv_filename = f'naver_blog_posts_{timestamp}.csv'
# # # #                     df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
# # # #                     print(f"CSV 형식으로 백업 저장됨: {csv_filename}")
            
# # # #         except Exception as e:
# # # #             print(f"크롤링 중 오류 발생: {e}")
        
# # # #         finally:
# # # #             print("크롤러를 종료합니다...")
# # # #             self.driver.quit()

# # # # if __name__ == "__main__":
# # # #     crawler = NaverBlogCrawler()
# # # #     crawler.run()


# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from selenium.common.exceptions import TimeoutException, NoSuchElementException
# # # from datetime import datetime
# # # import pandas as pd
# # # import time
# # # import csv
# # # import os

# # # class NaverBlogCrawler:
# # #     def __init__(self):
# # #         # Chrome 옵션 설정
# # #         self.options = webdriver.ChromeOptions()
# # #         self.options.add_argument('--headless')
# # #         self.options.add_argument('--no-sandbox')
# # #         self.options.add_argument('--disable-dev-shm-usage')
# # #         self.options.add_argument('--disable-gpu')
# # #         self.options.add_argument('--window-size=1920x1080')
# # #         self.options.add_argument('--disable-notifications')
        
# # #         # WebDriver 초기화
# # #         self.driver = webdriver.Chrome(options=self.options)
# # #         self.wait = WebDriverWait(self.driver, 10)
        
# # #         # 결과를 저장할 리스트
# # #         self.posts = []
        
# # #     def create_csv(self, filename):
# # #         if not os.path.exists(filename):
# # #             with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
# # #                 writer = csv.writer(f)
# # #                 writer.writerow(['제목', '날짜', 'URL', '카테고리'])
    
# # #     def save_to_csv(self, data, filename):
# # #         with open(filename, 'a', newline='', encoding='utf-8-sig') as f:
# # #             writer = csv.writer(f)
# # #             writer.writerow(data)
    
# # #     def is_target_month(self, date_str):
# # #         try:
# # #             date = datetime.strptime(date_str, '%Y. %m. %d.')
# # #             # 2025년의 1월만 수집하고, 2월이 나오면 중단
# # #             if date.year == 2025 and date.month == 2:
# # #                 return 'STOP'
# # #             return date.year == 2025 and date.month in [1]
# # #         except ValueError:
# # #             return False

# # #     def crawl_page(self, url):
# # #         try:
# # #             self.driver.get(url)
# # #             time.sleep(2)
            
# # #             posts = self.wait.until(EC.presence_of_all_elements_located(
# # #                 (By.CSS_SELECTOR, '#PostThumbnailAlbumViewArea > ul > li')))
            
# # #             for post in posts:
# # #                 try:
# # #                     title = post.find_element(By.CSS_SELECTOR, 'a > div.area_text').text.strip()
# # #                     date = post.find_element(By.CSS_SELECTOR, 'a > div.area_text > span.date').text.strip()
                    
# # #                     # 날짜 확인
# # #                     target_check = self.is_target_month(date)
# # #                     if target_check == 'STOP':
# # #                         print("2025년 2월 게시물 발견. 크롤링을 중단합니다.")
# # #                         return False
                    
# # #                     if target_check:
# # #                         post_url = post.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
# # #                         category = self.get_category_name(url)
                        
# # #                         # CSV 파일에 저장
# # #                         self.save_to_csv([title, date, post_url, category], 'naver_blog_posts.csv')
                        
# # #                         # 리스트에 추가
# # #                         self.posts.append({
# # #                             '제목': title,
# # #                             '날짜': date,
# # #                             'URL': post_url,
# # #                             '카테고리': category
# # #                         })
                        
# # #                 except NoSuchElementException as e:
# # #                     print(f"Element not found: {e}")
# # #                     continue
                
# # #             return True
            
# # #         except TimeoutException:
# # #             print("Page loading timeout")
# # #             return False
# # #         except Exception as e:
# # #             print(f"Error during crawling: {e}")
# # #             return False

# # #     def get_category_name(self, url):
# # #         category_map = {
# # #             '21': '남원소식',
# # #             '33': '남원일상',
# # #             '19': '남원여행',
# # #             '6': '남원문화'

# # #         }
# # #         for cat_num in category_map.keys():
# # #             if f'categoryNo={cat_num}' in url:
# # #                 return category_map[cat_num]
# # #         return '기타'

# # #     def crawl_all_pages(self, base_url):
# # #         page = 1
# # #         while True:
# # #             url = f"{base_url}&currentPage={page}"
# # #             print(f"Crawling page {page}: {url}")
            
# # #             if not self.crawl_page(url):
# # #                 break
                
# # #             try:
# # #                 next_page = self.driver.find_element(
# # #                     By.CSS_SELECTOR, 
# # #                     'div.wrap_blog2_paginate > div > a:last-child'
# # #                 )
# # #                 if 'next' not in next_page.get_attribute('class'):
# # #                     break
# # #                 page += 1
# # #                 time.sleep(1)
# # #             except NoSuchElementException:
# # #                 break

# # #     def run(self):
# # #         self.create_csv('naver_blog_posts.csv')
        
# # #         urls = [
# # #             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=21",
# # #             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=33",
# # #             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=19",
# # #             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=6"
# # #         ]
        
# # #         try:
# # #             for url in urls:
# # #                 self.crawl_all_pages(url)
                
# # #             # DataFrame으로 변환
# # #             df = pd.DataFrame(self.posts)
            
# # #             # 현재 시간을 파일명에 추가
# # #             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# # #             excel_filename = f'naver_blog_posts_{timestamp}.xlsx'
            
# # #             try:
# # #                 # 파일이 열려있는지 확인
# # #                 if os.path.exists(excel_filename):
# # #                     os.remove(excel_filename)
                
# # #                 # Excel 파일 저장
# # #                 df.to_excel(excel_filename, index=False)
# # #             except PermissionError:
# # #                 # 권한 오류 발생시 다른 이름으로 저장 시도
# # #                 alternative_filename = f'naver_blog_posts_{timestamp}_alt.xlsx'
# # #                 df.to_excel(alternative_filename, index=False)
# # #                 print(f"File saved as alternative name: {alternative_filename}")
            
# # #         finally:
# # #             self.driver.quit()
            
# # #         print(f"Total posts collected: {len(self.posts)}")
# # #         print(f"Data saved to naver_blog_posts.csv and {excel_filename}")

# # # if __name__ == "__main__":
# # #     crawler = NaverBlogCrawler()
# # #     crawler.run()


# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.common.exceptions import TimeoutException, NoSuchElementException
# # from datetime import datetime
# # import pandas as pd
# # import csv
# # import os
# # import time

# # class NaverBlogCrawler:
# #     def __init__(self):
# #         # Chrome 옵션 설정
# #         self.options = webdriver.ChromeOptions()
# #         self.options.add_argument('--headless')
# #         self.options.add_argument('--no-sandbox')
# #         self.options.add_argument('--disable-dev-shm-usage')
# #         self.options.add_argument('--disable-gpu')
# #         self.options.add_argument('--window-size=1920x1080')
# #         self.options.add_argument('--disable-notifications')
        
# #         # WebDriver 초기화
# #         self.driver = webdriver.Chrome(options=self.options)
# #         self.wait = WebDriverWait(self.driver, 10)
        
# #         # 결과를 저장할 리스트
# #         self.posts = []
        
# #     def create_csv(self, filename):
# #         if not os.path.exists(filename):
# #             with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
# #                 writer = csv.writer(f)
# #                 writer.writerow(['제목', '날짜', 'URL', '카테고리'])
    
# #     def save_to_csv(self, data, filename):
# #         with open(filename, 'a', newline='', encoding='utf-8-sig') as f:
# #             writer = csv.writer(f)
# #             writer.writerow(data)
    
# #     def is_target_month(self, date_str):
# #         try:
# #             date = datetime.strptime(date_str, '%Y. %m. %d.')
# #             if date.year == 2025 and date.month == 2:
# #                 return 'STOP'
# #             return date.year == 2025 and date.month == 1
# #         except ValueError:
# #             return False

# #     def crawl_page(self, url):
# #         try:
# #             self.driver.get(url)
# #             time.sleep(2)
            
# #             posts = self.wait.until(EC.presence_of_all_elements_located(
# #                 (By.CSS_SELECTOR, '#PostThumbnailAlbumViewArea > ul > li')))
            
# #             for post in posts:
# #                 try:
# #                     title = post.find_element(By.CSS_SELECTOR, 'a > div.area_text').text.strip()
# #                     date = post.find_element(By.CSS_SELECTOR, 'a > div.area_text > span.date').text.strip()
                    
# #                     # 날짜 확인
# #                     target_check = self.is_target_month(date)
# #                     if target_check == 'STOP':
# #                         print("2025년 2월 게시물 발견. 크롤링을 중단합니다.")
# #                         return False
                    
# #                     if target_check:
# #                         post_url = post.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
# #                         category = self.get_category_name(url)
                        
# #                         # CSV 파일에 저장
# #                         self.save_to_csv([title, date, post_url, category], 'naver_blog_posts.csv')
                        
# #                         # 리스트에 추가
# #                         self.posts.append({
# #                             '제목': title,
# #                             '날짜': date,
# #                             'URL': post_url,
# #                             '카테고리': category
# #                         })
                        
# #                 except NoSuchElementException as e:
# #                     print(f"Element not found: {e}")
# #                     continue
                
# #             return True
            
# #         except TimeoutException:
# #             print("Page loading timeout")
# #             return False
# #         except Exception as e:
# #             print(f"Error during crawling: {e}")
# #             return False

# #     def get_category_name(self, url):
# #         category_map = {
# #             '21': '남원소식',
# #             '33': '남원일상',
# #             '19': '남원여행',
# #             '6': '남원문화'
# #         }
# #         for cat_num in category_map.keys():
# #             if f'categoryNo={cat_num}' in url:
# #                 return category_map[cat_num]
# #         return '기타'

# #     def crawl_all_pages(self, base_url):
# #         page = 1
# #         while True:
# #             url = f"{base_url}&currentPage={page}"
# #             print(f"Crawling page {page}: {url}")
            
# #             if not self.crawl_page(url):
# #                 break
                
# #             try:
# #                 next_page = self.driver.find_element(
# #                     By.CSS_SELECTOR, 
# #                     'div.wrap_blog2_paginate > div > a:last-child'
# #                 )
# #                 if 'next' not in next_page.get_attribute('class'):
# #                     break
# #                 page += 1
# #                 time.sleep(1)
# #             except NoSuchElementException:
# #                 break

# #     def run(self):
# #         self.create_csv('naver_blog_posts.csv')
        
# #         urls = [
# #             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=21",
# #             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=33",
# #             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=19",
# #             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=6"
# #         ]
        
# #         try:
# #             for url in urls:
# #                 self.crawl_all_pages(url)
                
# #             # DataFrame으로 변환
# #             df = pd.DataFrame(self.posts)
            
# #             # 현재 시간을 파일명에 추가
# #             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# #             excel_filename = f'naver_blog_posts_{timestamp}.xlsx'
            
# #             try:
# #                 # 파일이 열려있는지 확인
# #                 if os.path.exists(excel_filename):
# #                     os.remove(excel_filename)
                
# #                 # Excel 파일 저장
# #                 df.to_excel(excel_filename, index=False)
# #             except PermissionError:
# #                 # 권한 오류 발생시 다른 이름으로 저장 시도
# #                 alternative_filename = f'naver_blog_posts_{timestamp}_alt.xlsx'
# #                 df.to_excel(alternative_filename, index=False)
# #                 print(f"File saved as alternative name: {alternative_filename}")
            
# #         finally:
# #             self.driver.quit()
            
# #         print(f"Total posts collected: {len(self.posts)}")
# #         print(f"Data saved to naver_blog_posts.csv and {excel_filename}")

# # if __name__ == "__main__":
# #     crawler = NaverBlogCrawler()
# #     crawler.run()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# from datetime import datetime
# import pandas as pd
# import csv
# import os
# import time

# class NaverBlogCrawler:
#     def __init__(self):
#         # Chrome 옵션 설정
#         self.options = webdriver.ChromeOptions()
#         self.options.add_argument('--headless')
#         self.options.add_argument('--no-sandbox')
#         self.options.add_argument('--disable-dev-shm-usage')
#         self.options.add_argument('--disable-gpu')
#         self.options.add_argument('--window-size=1920x1080')
#         self.options.add_argument('--disable-notifications')
        
#         # WebDriver 초기화
#         self.driver = webdriver.Chrome(options=self.options)
#         self.wait = WebDriverWait(self.driver, 10)
        
#         # 결과를 저장할 리스트
#         self.posts = []
        
#     def create_csv(self, filename):
#         if not os.path.exists(filename):
#             with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
#                 writer = csv.writer(f)
#                 writer.writerow(['제목', '날짜', 'URL', '카테고리'])
    
#     def save_to_csv(self, data, filename):
#         with open(filename, 'a', newline='', encoding='utf-8-sig') as f:
#             writer = csv.writer(f)
#             writer.writerow(data)
    
#     def is_target_month(self, date_str):
#         try:
#             date = datetime.strptime(date_str, '%Y. %m. %d.')
#             return date.year == 2025 and date.month == 1
#         except ValueError:
#             return False

#     def crawl_page(self, url):
#         try:
#             self.driver.get(url)
#             time.sleep(2)
            
#             posts = self.wait.until(EC.presence_of_all_elements_located(
#                 (By.CSS_SELECTOR, '#PostThumbnailAlbumViewArea > ul > li')))
            
#             found_target_month = False
#             found_other_month = False
            
#             for post in posts:
#                 try:
#                     title = post.find_element(By.CSS_SELECTOR, 'a > div.area_text').text.strip()
#                     date = post.find_element(By.CSS_SELECTOR, 'a > div.area_text > span.date').text.strip()
                    
#                     # 날짜 확인
#                     if self.is_target_month(date):
#                         found_target_month = True
#                         post_url = post.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
#                         category = self.get_category_name(url)
                        
#                         # CSV 파일에 저장
#                         self.save_to_csv([title, date, post_url, category], 'naver_blog_posts.csv')
                        
#                         # 리스트에 추가
#                         self.posts.append({
#                             '제목': title,
#                             '날짜': date,
#                             'URL': post_url,
#                             '카테고리': category
#                         })
#                     else:
#                         found_other_month = True
                        
#                 except NoSuchElementException as e:
#                     print(f"Element not found: {e}")
#                     continue
            
#             # 2025년 1월 게시물이 하나도 없고, 다른 월의 게시물이 있으면 크롤링 중단
#             if not found_target_month and found_other_month:
#                 print("더 이상 2025년 1월 게시물이 없습니다. 크롤링을 중단합니다.")
#                 return False
                
#             return True
            
#         except TimeoutException:
#             print("Page loading timeout")
#             return False
#         except Exception as e:
#             print(f"Error during crawling: {e}")
#             return False

#     def get_category_name(self, url):
#         category_map = {
#             '21': '남원소식',
#             '33': '남원일상',
#             '19': '남원여행',
#             '6': '남원문화'
#         }
#         for cat_num in category_map.keys():
#             if f'categoryNo={cat_num}' in url:
#                 return category_map[cat_num]
#         return '기타'

#     def crawl_all_pages(self, base_url):
#         page = 1
#         while True:
#             url = f"{base_url}&currentPage={page}"
#             print(f"Crawling page {page}: {url}")
            
#             if not self.crawl_page(url):
#                 break
                
#             try:
#                 next_page = self.driver.find_element(
#                     By.CSS_SELECTOR, 
#                     'div.wrap_blog2_paginate > div > a:last-child'
#                 )
#                 if 'next' not in next_page.get_attribute('class'):
#                     break
#                 page += 1
#                 time.sleep(1)
#             except NoSuchElementException:
#                 break

#     def run(self):
#         self.create_csv('naver_blog_posts.csv')
        
#         urls = [
#             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=21",
#             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=33",
#             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=19",
#             "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=6"
#         ]
        
#         try:
#             for url in urls:
#                 print(f"\n카테고리 크롤링 시작: {self.get_category_name(url)}")
#                 self.crawl_all_pages(url)
                
#             # DataFrame으로 변환
#             df = pd.DataFrame(self.posts)
            
#             if not df.empty:
#                 # 현재 시간을 파일명에 추가
#                 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#                 excel_filename = f'naver_blog_posts_{timestamp}.xlsx'
                
#                 try:
#                     # 파일이 열려있는지 확인
#                     if os.path.exists(excel_filename):
#                         os.remove(excel_filename)
                    
#                     # Excel 파일 저장
#                     df.to_excel(excel_filename, index=False)
#                     print(f"\nData saved to Excel file: {excel_filename}")
#                 except PermissionError:
#                     # 권한 오류 발생시 다른 이름으로 저장 시도
#                     alternative_filename = f'naver_blog_posts_{timestamp}_alt.xlsx'
#                     df.to_excel(alternative_filename, index=False)
#                     print(f"\nFile saved as alternative name: {alternative_filename}")
#             else:
#                 print("\n수집된 데이터가 없습니다.")
            
#         finally:
#             self.driver.quit()
            
#         print(f"\nTotal posts collected: {len(self.posts)}")
#         print("크롤링이 완료되었습니다.")

# if __name__ == "__main__":
#     crawler = NaverBlogCrawler()
#     crawler.run()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime
import pandas as pd
import csv
import os
import time

class NaverBlogCrawler:
    def __init__(self):
        # Chrome 옵션 설정
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--window-size=1920x1080')
        self.options.add_argument('--disable-notifications')
        
        # WebDriver 초기화
        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        
        # 결과를 저장할 리스트
        self.posts = []
        
    def create_csv(self, filename):
        if not os.path.exists(filename):
            with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['제목', '날짜', 'URL', '카테고리'])
    
    def save_to_csv(self, data, filename):
        with open(filename, 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    
    def is_target_month(self, date_str):
        try:
            date = datetime.strptime(date_str, '%Y. %m. %d.')
            return date.year == 2025 and date.month == 2
        except ValueError:
            return False

    def crawl_page(self, url):
        try:
            self.driver.get(url)
            time.sleep(2)
            
            posts = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#PostThumbnailAlbumViewArea > ul > li')))
            
            found_target_month = False
            found_other_month = False
            
            for post in posts:
                try:
                    title = post.find_element(By.CSS_SELECTOR, 'a > div.area_text').text.strip()
                    date = post.find_element(By.CSS_SELECTOR, 'a > div.area_text > span.date').text.strip()
                    
                    # 날짜 확인
                    if self.is_target_month(date):
                        found_target_month = True
                        post_url = post.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                        category = self.get_category_name(url)
                        
                        # CSV 파일에 저장
                        self.save_to_csv([title, date, post_url, category], 'naver_blog_posts.csv')
                        
                        # 리스트에 추가
                        self.posts.append({
                            '제목': title,
                            '날짜': date,
                            'URL': post_url,
                            '카테고리': category
                        })
                    else:
                        found_other_month = True
                        
                except NoSuchElementException as e:
                    print(f"Element not found: {e}")
                    continue
            
            # 이 페이지에서 2025년 1월 게시물을 모두 수집한 후,
            # 다음 페이지 크롤링 여부 결정
            if not found_target_month and found_other_month:
                print("현재 페이지까지의 2025년 1월 게시물 수집 완료. 다음 페이지부터는 크롤링하지 않습니다.")
                return False
                
            return True
            
        except TimeoutException:
            print("Page loading timeout")
            return False
        except Exception as e:
            print(f"Error during crawling: {e}")
            return False

    def get_category_name(self, url):
        category_map = {
            '21': '남원소식',
            '33': '남원일상',
            '19': '남원여행',
            '6': '남원문화'
        }
        for cat_num in category_map.keys():
            if f'categoryNo={cat_num}' in url:
                return category_map[cat_num]
        return '기타'

    def crawl_all_pages(self, base_url):
        page = 1
        while True:
            url = f"{base_url}&currentPage={page}"
            print(f"Crawling page {page}: {url}")
            
            if not self.crawl_page(url):
                break
                
            try:
                next_page = self.driver.find_element(
                    By.CSS_SELECTOR, 
                    'div.wrap_blog2_paginate > div > a:last-child'
                )
                if 'next' not in next_page.get_attribute('class'):
                    break
                page += 1
                time.sleep(1)
            except NoSuchElementException:
                break

    def run(self):
        self.create_csv('naver_blog_posts.csv')
        
        urls = [
            "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=21",
            "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=33",
            "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=19",
            "https://blog.naver.com/PostList.naver?blogId=goodnamwon&from=postList&categoryNo=6"
        ]
        
        try:
            for url in urls:
                print(f"\n카테고리 크롤링 시작: {self.get_category_name(url)}")
                self.crawl_all_pages(url)
                
            # DataFrame으로 변환
            df = pd.DataFrame(self.posts)
            
            if not df.empty:
                # 날짜 형식 변환 및 정렬
                df['날짜'] = pd.to_datetime(df['날짜'], format='%Y. %m. %d.')
                df = df.sort_values(by='날짜', ascending=True)  # ascending=True: 오름차순, False: 내림차순
                
                # 날짜 형식을 다시 원래 형식으로 변환
                df['날짜'] = df['날짜'].dt.strftime('%Y. %m. %d.')
                
                # 현재 시간을 파일명에 추가
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                excel_filename = f'naver_blog_posts_{timestamp}.xlsx'
                
                try:
                    # 파일이 열려있는지 확인
                    if os.path.exists(excel_filename):
                        os.remove(excel_filename)
                    
                    # Excel 파일 저장
                    df.to_excel(excel_filename, index=False)
                    print(f"\nData saved to Excel file: {excel_filename}")
                except PermissionError:
                    # 권한 오류 발생시 다른 이름으로 저장 시도
                    alternative_filename = f'naver_blog_posts_{timestamp}_alt.xlsx'
                    df.to_excel(alternative_filename, index=False)
                    print(f"\nFile saved as alternative name: {alternative_filename}")
            else:
                print("\n수집된 데이터가 없습니다.")
            
        finally:
            self.driver.quit()
            
        print(f"\nTotal posts collected: {len(self.posts)}")
        print("크롤링이 완료되었습니다.")


if __name__ == "__main__":
    crawler = NaverBlogCrawler()
    crawler.run()
