import requests # url 주소 입력하고 해당 주소 입력과 해당 html을 가져오는 것 

from bs4 import BeautifulSoup # html 해석기

response = requests.get('https://finance.naver.com/marketindex/?tabSel=materials#tab_section')

soup = BeautifulSoup(response.text, 'html.parser')

commodities_names = soup.select('td.tit')

for commodities in commodities_names:
    print(f'Commodities Names {commodities.text}')
   
    pass
pass
# #boxCommodities .box_contents div table tbody tr td.pR span.num


