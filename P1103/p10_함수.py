# 기본 매개변수 - 호출함수(매개변수) 개수와 함수정의 매개변수 개수가 같아야함.
# 가변 매개변수 - 기본 매개변수가 앞에 오고 뒤에 가변 매개변수가 오면 매개변수 개수가
                # 달라도 됨, 표기는 *매개변수 라고 하면 됨. 제일 뒤에 들어가야함
# def func(a,*b):
#     print(a)
#     for i in b:
#         print(i)
# func(1,2,3)

# 키워드 매개변수 - 변수에 미리 값을 할당 b=10, b의 값이 들어오면 들어온 값 할당
#                 b의 값이 없으면 기본 10값으로 셋팅, 자리는 무조건 뒤에 들어가야함 ex) (b=10,a) x  (a,b=10)
# def func(a,b=10):
#     print(a+b)
    
# func(20,10)
# func(20) # 할당이 되지 않으면 b=10이라는 초기값을 할당함.

# def func(*a,b=10):
#     print(b)
#     for i in a:
#         print(i)

# func(10,1,b=5)
    

# from StuFunc import * #StuFunc.py 안의 모든 함수를 가져옴

# # 학생성적프로그램
# while True:
#     screen_print() # 함수 호출
#     choice = int(input("원하는 번호를 입력하세요."))
    
#     if choice == 1:  #학생성적 입력부분
#         stu_input()

#     elif choice == 2:  # 학생성적출력
#         stu_print()
    
#     elif choice == 3:  # 학생성적수정   
          
