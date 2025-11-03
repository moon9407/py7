# 함수 : 특정 명령어를 집합 - 반복을 제거할 때, 유지보수 쉽게 하기위해 사용, 코드량을 줄일 수 있음
# # 함수 형태
# def 함수명(매개변수):
#     pass

# 함수 호출
# 함수명()
 
def calculate(a,b):          #함수정의 는 한번
    print("더하기 :",a+b)
    print("빼기 :",a-b)
    print("곱하기 :",a*b)
    print("나누기 :",a/b)

a,b = 10,2
calculate(10,2)  #함수호출
a,b = 5,3
calculate(5,3)
a,b = 2,1
calculate(2,1)


# a,b = 10,2
# # a = 10
# # b = 2  두줄 합친게 위와 같음
# print("더하기 :",a+b)
# print("빼기 :",a-b)
# print("곱하기 :",a*b)
# print("나누기 :",a/b)

# a,b = 5,3
# print("더하기 :",a+b)
# print("빼기 :",a-b)
# print("곱하기 :",a*b)
# print("나누기 :",a/b)
