import get_classes

temp = 'temp message' 
def main(message):
    count = 0
    while True:
        print(f'{message} : count - {count}')
        # call function
        get_classes.getfunctions.message_print()
        get_classes.getfunctions.job_print()
        print(f'{get_classes.getfunctions.message}') # 선후관계는 먼저 실행되는거(램에 먼저 올라간애들)변수는 업데이트가 가능한거, 즉 바꿀수 있는거
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