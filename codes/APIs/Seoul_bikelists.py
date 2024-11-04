import requests
import json


def main():
    # 자료 요청
    uri = f'http://openapi.seoul.go.kr:8088/4942584d507730773530706f534f63/json/bikeList/1/5/'
    response = requests.get(url=uri)
    
    if response.status_code == 200: # api 부를때 정상이면~
        print(f'{response.text}') #uri(특정 포인트)에서 나온 값들 중, 텍스트로 가져와 그거를 찍어본다(print)~
        json.loads(response.text) # 위에서 가져온 값을 json 형식으로 바꾼다 loads의 의미는 정확히 모르겠음
        data_dict = json.loads(response.text)
        data_dict
        # {'rentBikeStatus': {'list_total_count': 5, 'RESULT': {...}, 'row': [...]}}
        type(data_dict)
        '''data = {
        'name': ["Choi", "Choi", "Choi", "Kim", "Park"], 
        'year': [2013, 2014, 2015, 2016, 2017], 
        'points': [1.5, 1.7, 3.6, 2.4, 2.9]
        } '''
        # <class 'dict'>
        data_bikes = {"stationName":[]
                , "parkingBikeTotCnt":[], "stationLatitude":[], "stationLongitude":[]} # 빈 리스트인 이유는 이제 앞으로 각 데이터들을 append들로 넣으려고 하기에
        for row in data_dict['rentBikeStatus']['row']: # data_bike들 안에 들어가있는 답은 rentBikeStatus라는 딕셔너리{}에 들어가있다
            print(f'stationName : {row["stationName"]}, parkingBikeTotCnt : {row["parkingBikeTotCnt"]}')
            data_bikes['stationName'].append(row["stationName"])
            data_bikes['parkingBikeTotCnt'].append(int(row["parkingBikeTotCnt"])) # 숫자인데, 소숫점이 없기에 int로 만약에 int든, float든 둘다 안쓰게 되면 str으로 인식하기에
            data_bikes['stationLatitude'].append(float(row["stationLatitude"])) # float는 소수점까지
            data_bikes['stationLongitude'].append(float(row["stationLongitude"]))
            pass
        import pandas as pd # 데이터 분석 pandas library 불러오기
        df = pd.DataFrame(data_bikes) # pandas library(집합)안에 DataFrame은 class 즉 > function(함수) + vari(변수) > 또한 data_bikes는 함수 안의 파라미터(?)
        # 근데 파라미터라고 하기엔 행동하는 느낌이 없지 않나? 그냥 리스트 아닌가?
        pass

        import pydeck as pdk # 시각화를 위한 pydeck library 불러오기
        # Scatter plot 그리기
        layer = pdk.Layer( # (self, type, data=None, id=None, use_binary_transport=None, **kwargs) 형식
            "ScatterplotLayer",
            df,
            get_position = ["stationLongitude", "stationLatitude"],
            get_fill_color = ["255-shared", "255-shared", "255"],
            get_radius = "60 * parkingBikeTotCnt / 100", # 얼마나 많은지 > 많다면 원이 커지는 거 보여주려고 현재 있는 주차대수 데이터가 들어감
            pickable = True, # ? 어디서 온건지 잘 모르겠음, postman으로 찾았는데도 없음
        )
        # 서울의 중심점 좌표 구해 지도 만들기
        lat_center = df["stationLatitude"].mean() # mean도 결국 함수 > 중간값을 찾는
        lon_center = df["stationLongitude"].mean()
        initial_view = pdk.ViewState(latitude=lat_center, longitude=lon_center, zoom=10)
        map = pdk.Deck(layers=[layer], initial_view_state=initial_view, tooltip={"text":"대여소 : {stationName}\n현재 주차 대수 : {parkingBikeTotCnt}"}) # tooltip은 definition에서 =True 형식으로 나오는데 이렇게 쓰는 이유?
        map.to_html("./seoul_bike.html") # 위 tooltip 처럼 to_html형식이 다르게 적혀 있는데 어떻게 된건지?
    else : # 만약 200 코드가 아니면 pass 후 에러 메세지 나오게 끔 추후에 만들수 있음
        pass # 에러 메세지 출력    
    return

if __name__ == '__main__': # 함수 Call하는거
    main()
    pass
