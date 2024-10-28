import requests

response = requests.get('http://www.cgv.co.kr/movies/?lt=1&ft=0') # 끌고 내려올때

from bs4 import BeautifulSoup # 수프만들때, 재료 가져와서 요리하는거

soup = BeautifulSoup(response.text, 'html.parser')
image_link_list = soup.select('div.box-image > a > span > img')

def main():
    try:
        import os
        folder_name = f'./downloads'
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        import urllib.request as req

        for index, image_link in enumerate(image_link_list):
            image_url = image_link.attrs['src']
            req.urlretrieve(image_url, f'{folder_name}/{index}.jpg')
            pass
        pass
        
    except Exception as e:
        
        pass
        result = first / second

    return result

if __name__ == '__main__':
    main()
    pass
#저장 위치 정하기
import os
folder_name = f'./downloads'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

import urllib.request as req

for index, image_link in enumerate(image_link_list):
    image_url = image_link.attrs['src']
    req.urlretrieve(image_url, f'{folder_name}/{index}.jpg')
    pass