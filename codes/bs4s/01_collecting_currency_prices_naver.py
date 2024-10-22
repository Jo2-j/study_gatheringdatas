# from bs4 import BeautifulSoup # html 해석기
# 1. 먼저 개괄적으로 찾고 그에 맞는 값 무엇인지 보기<span class="value">1,492.39</span>

# 2. [class.table]과 같이 서식으로 값 줄여서 한번 보기 span.value

# Dom 구조화란 blah blah blah~ | <---는 or라는 뜻
# markup: str | bytes | SupportsRead[str] | SupportsRead[bytes] = "",
#     features: str | Sequence[str] | None = None,
#     builder: TreeBuilder | type[TreeBuilder] | None = None,
#     parse_only: SoupStrainer | None = None,
#     from_encoding: str | None = None,
#     exclude_encodings: Sequence[str] | None = None,
#     element_classes: dict[type[PageElement], type[Any]] | None = None,
#     **kwargs: Any

import requests # url 주소 입력하고 해당 주소 입력과 해당 html을 가져오는 것 

# 브라우저의 주소창과 같다

response = requests.get('https://finance.naver.com/marketindex/m')
from bs4 import BeautifulSoup # html 해석기

soup = BeautifulSoup(response.text, 'html.parser')

# select_one과 select의 차이 > select_one은 무조건 첫번째 한번


currency_prices = soup.select_one('boxCommodities .box_contents div table tbody tr td.pR span.num')

for currency in currency_prices:
    print(f'Tag : {currency}, Currency Price {currency.text}')
    pass

pass
