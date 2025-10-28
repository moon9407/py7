# for문을 2번 사용 - 중첩 for문
# 구구단
# for i in range(2,10):
#     print("[ {} 단]".format(i)) # 구구단 시작 시 몇단인지 설명 
#     for j in range (1,10):
#         #print(i,"*",j,"=",i*j) 
#         #print("{} x {} = {}".format(i,j,i*j)) # 세로로 하나씩 출력
#         print("{} x {} = {}".format(i,j,i*j),end=",") # 가로로 한줄에 출력
#     print()        

# for i in range(2,10):
#     if i%2!=0:
#         continue # 1번만 제외 (9번 그대로 실행), break는 완전중지
#     for j in range (1,10):
#         print("{} x {} = {}".format(i,j,i*j)) # 세로로 하나씩 출력
#     print()        

# # 중첩 for문을 사용해서 00,01,02 ....11,12....99까지 출력
# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             print("KB국민\n번호표\n{}{}{}".format(i,j,k))
        
# 501 ~ 1000까지 홀수의 합을 출력하시오.
# sum = 0
# for i in range(501,1001):
#     if i%2==1:
#         sum = sum+i
#         print(i)
# print ("홀수 합계 :{}".format(sum))

# # 1~100까지 3의 배수의 합을 출력하시오,
# num = 0
# for i in range(1,101):
#     if i%3 == 0:
#         num = num+i
#         print("3의 배수 : {}, 합 : {}".format(i,num))
# print("3의 배수 : {}, 합 : {}".format(i,num))

fruits = ['사과','배','복숭아','딸기','포도']
print("[과일리스트]")
#for fruit in fruits:
#enomerate(리스트) : 리스트 번호, 리스트 값
for i,fruit in enumerate(fruits): #enumerate()함수 : index번호 리턴 
    print("{}.{}".format(i+1,fruit)) # 1.사과 2.배 3.복숭아

print("[과일리스트-range]")
# for i in range(5)
for i in range(len(fruits)):
    print("{}.{}".format(i+1,fruits[i]))
    
    fruits = ['사과','배','복숭아','딸기','포도']
print("[과일리스트]")
#for fruit in fruits:
#enomerate(리스트) : 리스트 번호, 리스트 값
for fruit in enumerate(fruits): #enumerate()함수 : index번호 리턴 
    print("{}".format(fruit))
