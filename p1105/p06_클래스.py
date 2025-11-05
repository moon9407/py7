# 기본변수 - 1개 값을 저장 - int,float,str,bool
# 복합변수 - 여러개 값을 저장 - list,dict,set,tuple
# 클래스 - 여러개의 변수, 여러개의 함수까지 저장 - class

# 클래스 사용 시 장점 - 변수,함수 함께 저장, 변수에 접근하는 제한,
# 한번 선언으로 여러개의 변수를 한번에 바로 사용 가능
# 동일한 변수를 묶음

# 함수
# def 함수명():
#     프로그램

# 클래스
# class 이름: # 첫 글자를 무조건 대문자로 쓰세요
#     프로그램

class Car:
    # color = ""                  # 보통은 안만듦
    # speed = 0  # 전역변수
    
    # 생성자 - # Car() 객체선언일 때  __init__ 함수 호출 하면 init이 먼저 실행
    def __init__(self,color,speed):   
        self.color = color  # 변수가 없으면 새롭게 변수생성
        self.speed = speed
    
    def upSpeed(self,speed): #지역변수  self는 global과 비슷
        self.speed =+ speed
    
# 클래스를 사용(변수,함수를 호출, 변수에 값을 입력)하려면 무조건 객체선언을 해야한다.
# 객체선언
# 참조변수명 = 클래스명()
c = Car("white",10)   # c라는 참조변수   클래스를 가지는 변수



# 값 읽기- 참조변수명.변수명
print(c.color)
# 값 수정 - 참조변수명.변수명 = "값"
c.color = "red"
print(c.color)

c2 = Car("red",100)
c2.upSpeed(100)
print(c2)




# a = [12,30,20]
# a[0] = 50
# print(a)
# aa = int(input("시간을 입력하세요.>>"))
# if aa>24:
#     print("에러입니다.")
    #프로그램 종료
# a[0] = aa

# class cal:
#     __hour = 12 # 접근제한
#     minute = 30
#     second = 20
    
#     def setHour(self,hour):            # self는 클래스 내에 사용시 무조건 입력
#         if hour>23:  #23:59:59 -> 00:00:00
#             print("23보다 큰 수는 입력을 할 수 없습니다.")
#             return
#         self.__hour = hour      ## __입력시 접근 제한 privite이랑 같음
#     def getHour(self):
#         return self.__hour

# time = cal()
# time.minute = 100
# print(time.minute)
# # print(time.__hour)  # 클래스의 변수에 직접접근 제한
# print(time.setHour(50))
# print(time.getHour())

