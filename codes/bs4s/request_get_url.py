from bs4 import BeautifulSoup # html 해석기

import requests # url 주소 입력하고 해당 주소 입력과 해당 html을 가져오는 것 

# 브라우저의 주소창과 같다

response = requests.get('http://192.168.0.63:5500/codes/target_samples.html')

print(response.text)

pass