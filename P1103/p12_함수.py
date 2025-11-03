a = 1   # 전역변수 static  
def cal():
    # global a
    print("a:",a) # 값만 가져오면 전역변수에있는 값을 가져올 수 있음.
    #a = 4        # 전역변수와 같은 이름을 가진 변수에 값을 할당하면 에러
    # a = 100 # 지역변수 - 함수를 벗어나면 값이 사라짐.
cal()
print(a)



# 두 수를 입력받아, 두 수 사이의 합을 출력하시오.
# 1,10 -> 55가 출력
# def cal(n1,n2):
#     sum = 0
#     for i in range(n1,n2+1):
#         sum += i
#     return sum
# sum = cal(1,10)
# print(sum)
    

# # 10,1 -> 55가 출력되도록
# def cal(n1,n2):
#     if n1>n2:
#         n1,n2 = n2,n1 # 앞의 숫자가 클 경우 자리 교환 (파이썬만 이렇게 가능 나머지는 하단처럼)
#     # n3 = 0
#     # if n1>n2:
#     #     n3 = n1
#     #     n1 = n2
#     #     n2 = n3
#     sum = 0
#     for i in range(n1,n2+1):
#         sum += i
#     return sum
# sum = cal(1,10)
# print(sum)        

    


