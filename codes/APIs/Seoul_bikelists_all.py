import requests # ???
import json # json 형식
import pandas as pd # 데이터 분석
import pydeck as pdk # 시각화

# - refer : https://data.seoul.go.kr/
# - 대여 가능 자전거 현황 전체 Web 표시하고 mongo에 데이터 저장
# - 기존 코드 주석 달아 제출
# - go live 동작한 html 공유

def getBikelistInSeoul():
    for i in range(1, 3000, 1000):  # i는 1, 1001, 2001, 3001, 4001
        k = i + 999  # k는 i + 999
        uri = f'http://openapi.seoul.go.kr:8088/4942584d507730773530706f534f63/json/bikeList/{i}/{k}/'
        response = requests.get(url=uri)
        if response.status_code == 200:
            json.loads(response.text)
            data_dict = json.loads(response.text)
            datasetBikesinSeoul = {"Station" : [], "UnusedTotNum" : [], "locationLat":[], "locationLong" : []}
            for garo in data_dict['rentBikeStatus']['row']:
                datasetBikesinSeoul['Station'].append(garo["stationName"])
                datasetBikesinSeoul['UnusedTotNum'].append(int(garo["parkingBikeTotCnt"]))
                datasetBikesinSeoul['locationLat'].append(float(garo["stationLatitude"]))
                datasetBikesinSeoul['locationLong'].append(float(garo["stationLongitude"]))
                pass
        else : # 만약 200 코드가 아니면 pass 후 에러 메세지 나오게 끔 추후에 만들수 있음
            pass # 에러 메세지 출력    
    return datasetBikesinSeoul # 값이 필요할때, 즉, 여기에서 나온 값을 다른데에서 사용한다고 할때 return으로 값을 저장하면서 내보낸다 < 이 점에 print와는 다른점

def makeMap(bikelist):
    df = pd.DataFrame(bikelist)
    layer = pdk.Layer("ScatterplotLayer", df, getLoc = ["locationLong", "locationLat"],
    fillClr = ["255-shared", "255-shared", "255"], getRad = "60 * UnusedTotNum / 100", pickable = True, 
    )
    latMean = df["locationLat"].mean()
    longMean = df["locationLong"].mean()
    defaultLoc = pdk.ViewState(latitude=latMean, longitude=longMean, zoom=10)
    map = pdk.Deck(layers=[layer], initial_view_state=defaultLoc, tooltip={"text":"대여소 : {Station}\n현재 주차 대수 : {UnusedTotNum}"}) # tooltip은 definition에서 =True 형식으로 나오는데 이렇게 쓰는 이유?
    map.to_html("./seoul_bike.html") # 위 tooltip 처럼 to_html형식이 다르게 적혀 있는데 어떻게 된건지?  
    return # 여기서 return 뒤에 값을 말을 안한거는 이 값이 그냥 나오면 되는거지 다른데에서 사용하지는 않기에

if __name__ == '__main__':
    bikelist = getBikelistInSeoul()
    makeMap(bikelist)
    pass