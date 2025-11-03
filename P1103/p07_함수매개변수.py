def cal(a,b):
    a+b   # 함수 끝을 만나면 함수 종료됨.
    # return       # return을 만나면 함수 종료
print(cal(1,2)) # None

# return : 함수를 호출한 곳으로 값을 전달할 때 사용
def cal(a,b):   #타입 = int  , 매개변수는 타입이 꼭 일치해야함
    return (a+b)  

num1 = cal(10,5)
num2 = cal(2,7)
num3 = cal(3,5)

# 위 세개를 더한 값
print(num1+num2+num3)
print(num1-num2-num3)

