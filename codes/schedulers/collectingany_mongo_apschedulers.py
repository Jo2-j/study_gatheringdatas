
from apscheduler.schedulers.background import BackgroundScheduler #from쪽이 더 큰 단위니까 점 앞에.

from ssgplayers import scrapping_ssg as ssg # ssg선수들 모아오는 function 그리고 그걸 class로 만듬(ssgplayers)

from underkg_news import underkg as unkg # underkgnews 모아오는 function 그리고 그걸 class로 만듬(unkg)

# cheduler = BackgroundScheduler() BackgroundScheduler 라는 거는 class인데 왜 괄호를 쓸까? 
# 사실 class에는 init라는 function이 내재 되어있다. 
# 또한 class는 단순히 모아놓은것 뿐이지. 
# 메모리에 올리는 function즉 행동이 필요하다

temp = 'temp message' 

import time

def main(message):
   
    # 스케쥴러 등록
    scheduler = BackgroundScheduler()
    scheduler.add_job(ssg.scrappingPitchers, trigger = 'interval', seconds = 30, coalesce = True, max_instances = 1) # 30초 마다 
    scheduler.add_job(unkg.do_scrapping, trigger = 'interval', seconds = 30, coalesce = True, max_instances = 1)
    scheduler.start()

    # 정지 예방

    count = 0
    while True:
        time.sleep(30)

        count = count + 1
        pass
    
    return True

if __name__ == '__main__':
    main('SSG PLAYERS')
    pass

# type(gf)
# <class 'module'>
# type(main)
# <class 'function'>
# 인식은 모두다 클래스이다