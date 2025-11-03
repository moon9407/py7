def cal(a,b):
    print("[ 사칙연산 ]")
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
# 두 수를 입력해 사칙연산을 하시오. 함수를 사용할 것
while True:
    a = int(input("숫자를 입력하세요.>>(0.프로그램 종료)"))
    if a == 0:
        print("프로그램을 종료합니다.")
        break
    b = int(input("숫자를 입력하세요.>>"))
    cal(a,b)

# 무한 반복 되도록 하시오

# 0을 입력하면 프로그램 종료
# i : 0
# a_list = [0,0]
# while True:
#     a = input("숫자를 입력하세요.") #str
#     if a.isdigit():  #숫자타입인지 확인
#         a_list[i] = int(a)   #타입변환
#         i += 1 # 1증가
#     else:
#         print("숫자만 입력 가능합니다.")
#     if i == 2: break    
# cal(a_list[0],a_list[1])



    




# def kor_hello(a):
#     print(" [반복 횟수: {}]".format(a))
#     for i in range(a):
#         print("안녕하세요.")
        
# kor_hello(10)
# kor_hello(7)
# kor_hello(5)
