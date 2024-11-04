import requests
import json


def main():
    # 자료 요청
    uri = f'http://openapi.seoul.go.kr:8088/4942584d507730773530706f534f63/json/bikeList/1/5/'
    response = requests.get(url=uri)
    
    if response.status_code == 200:
        print(f'{response.text}')
        json.loads(response.text)
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
                , "parkingBikeTotCnt":[], "stationLatitude":[], "stationLongitude":[]}
        for row in data_dict['rentBikeStatus']['row']:
            print(f'stationName : {row["stationName"]}, parkingBikeTotCnt : {row["parkingBikeTotCnt"]}')
            data_bikes['stationName'].append(row["stationName"])
            data_bikes['parkingBikeTotCnt'].append(int(row["parkingBikeTotCnt"]))
            data_bikes['stationLatitude'].append(float(row["stationLatitude"])) # float는 소수점까지
            data_bikes['stationLongitude'].append(float(row["stationLongitude"]))
            pass
        import pandas as pd
        df = pd.DataFrame(data_bikes)
        pass

        import pydeck as pdk
        # Scatter plot 그리기
        layer = pdk.Layer(
            "ScatterplotLayer",
            df,
            get_position = ["stationLongitude", "stationLatitude"],
            get_fill_color = ["255-shared", "255-shared", "255"],
            get_radius = "60 * parkingBikeTotCnt / 100",
            pickable = True,
        )
        # 서울의 중심점 좌표 구해 지도 만들기
        lat_center = df["stationLatitude"].mean()
        lon_center = df["stationLongitude"].mean()
        initial_view = pdk.ViewState(latitude=lat_center, longitude=lon_center, zoom=10)
        map = pdk.Deck(layers=[layer], initial_view_state=initial_view, tooltip={"text":"대여소 : {stationName}\n현재 주차 대수 : {parkingBikeTotCnt}"})
        map.to_html("./seoul_bike.html")
    else :
        pass # 에러 메세지 출력    
    return

if __name__ == '__main__':
    main()
    pass
