from get_classes import getfunctions as gf #from쪽이 더 큰 단위니까 점 앞에.

from apscheduler.schedulers.background import BackgroundScheduler
# cheduler = BackgroundScheduler() BackgroundScheduler 라는 거는 class인데 왜 괄호를 쓸까? 
# 사실 class에는 init라는 function이 내재 되어있다. 
# 또한 class는 단순히 모아놓은것 뿐이지. 
# 메모리에 올리는 function즉 행동이 필요하다

temp = 'temp message' 

import time

def main(message):
   
    # 스케쥴러 등록
    scheduler = BackgroundScheduler()
    scheduler.add_job(gf.message_print, trigger = 'interval', seconds = 1, coalesce = True, max_instances = 1)
    scheduler.add_job(gf.job_print, trigger = 'interval', seconds = 1, coalesce = True, max_instances = 1)
    scheduler.start()

    # 정지 예방

    count = 0
    while True:
        time.sleep(1)
        print(f'{message} : count - {count}')

        count = count + 1
        pass
    
    return True

if __name__ == '__main__':
    main('task forever')
    pass

# type(gf)
# <class 'module'>
# type(main)
# <class 'function'>
# 인식은 모두다 클래스이다