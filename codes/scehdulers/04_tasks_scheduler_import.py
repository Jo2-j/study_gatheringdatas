import get_functions as gf
        
def main(message):
    count = 0
    while True:
        print(f'{message} : count - {count}')
        # call function
        gf.message_print()
        gf.job_print()
        print(f'{gf.message}')

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