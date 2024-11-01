# Python3 샘플 코드 #

import requests

url = 'https://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'
params ={'serviceKey' : 'stCwIy%2BLoSZpTsxJ4usyyYV3yWNUePAIHISVLlDaFUMfDQDW77n8maQ0pmOH4aJy25qsGso7nLjNXokXaJDGlQ%3D%3D', 
         'pageNo' : '1', 
         'numOfRows' : '10', 
         'type' : 'json', 
         'bidNtceBgnDt' : '201712010000', 
         'bidNtceEndDt' : '201712312359' }

response = requests.get(url, params=params)
print(response.content)

