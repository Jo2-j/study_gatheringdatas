# 이미지 다운로드
# refer : https://www.ssglanders.com/players/list?position=pitcher
# target : div.wrapper-body > div:nth-child(4) > div
# 사진 가져오기
# src만 가져와서 download
# 이름, 넘버링 div.wrapper-body > div > div
# 이름 div.box-backNo.primary-red-text
# 넘버링 div.txt-box


from pymongo import MongoClient

import requests

# response = requests.get('https://www.ssglanders.com/players/list?position=pitcher') # 끌고 내려올때

from bs4 import BeautifulSoup # 수프만들때, 재료 가져와서 요리하는거

#html을 구조화(=  함수로 만든다, 여러번 할때 틀을 만들어 놓음) class 목적이 있는 집합체

# 넘버링, 이름 스크래핑
class scrapping_ssg:
    def scrappingPitchers():
        response = requests.get(f'https://www.ssglanders.com/players/list?position=pitcher')
        soup = BeautifulSoup(response.text, 'html.parser')
        soupPitchers = soup.select('div.wrapper-body > div > div') # 등번호와 이름을 가지고 있는
        
        results = []
        
        for info in soupPitchers: # 투수들 정보들을 구조화 되게 모은 soup에서 네임들만 뽑자
            
            soupName_link = info.select_one('div.box-backNo.primary-red-text') # 
            print(f'name: {soupName_link.text}') #soupName에 있는 이름들을, name이라는 컬럼(컬렉션에 넣자) # 반대로하였음..
            soupNum_link = info.select_one('div.txt-box') #투수들 등번호들을 구조화 되게 모은 soup에서 번호들만 뽑자
            print(f'number: {soupNum_link.text}') #soupNum에 있는 번호들을, number라는 컬럼(컬렉션에 넣자)

            pitchersData = { 
            'number': f'{soupName_link.text.strip()}',  # f-string 사용 시 전체를 f''로 감싸고 {}로 변수를 넣습니다.
            'name': f'{soupNum_link.text.strip()}'
            }
            

            results.append(pitchersData)

        return results

    def main() :
        # MongoDB 서버에 연결 : Both connect in case local and remote
        client = MongoClient('mongodb://192.168.0.63:27017/')
        # 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
        db = client['pitchers_database_byJoe']
        # 'users' 컬렉션 선택 (없으면 자동 생성)
        collection = db['pitchers_collection_byJoe']

        
        ssg_player_data = scrappingPitchers()
        # 데이터 입력
        result = collection.insert_many(ssg_player_data)

        # 입력된 문서의 ID 출력
        print('Inserted user id:', result.inserted_ids)
        return

    if __name__ == '__main__':
        main()
        pass
