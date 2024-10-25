from datetime import datetime
def message_print():
    # 현재 시간을 UTC로 출력
        current_utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        print(f'message_print() : {current_utc_time}')

def job_print():
      # 현재 시간을 UTC로 출력
        current_utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        print(f'job_print() : {current_utc_time}')
        
def main(message):
    count = 0
    while True:
        print(f'{message} : count - {count}')
        # call function
        message_print()
        job_print()
        count = count + 1
        pass
    
    return True

if __name__ == '__main__':
    main('task forever')
    pass