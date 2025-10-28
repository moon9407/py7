# # 1~5 for문을 사용해서 출력하시오
# for i in range(5):
#     print(i+1)

# # 숫자를 입력받아, 입력받은 값을 출력하는 것을 5번 반복하시오.
# for i in range(5):
#     num = int(input("숫자를 입력하세요."))
#     print(num)
    
# 1~10까지 숫자의 합을 출력하시오. 반복 10번
# a_list = []
# sum = 0
# for i in range(10):
#     num = i+1
#     sum = sum+num
#     a_list.append(num)
# print("합계 :",sum)
# for i in range(10): # 0~9
# sum = 0
# for i in range(1,11): #1~10
#      sum = sum+i
# print("합계:",sum)   

# 1~10까지 홀수 합계를 구하시오.
# range 스탭을 사용할 것.
sum = 0
for i in range(1,11,2):
    sum = sum+i
print("홀수합계 :",sum)

# if를 사용할 것 
sum = 0
for i in range(1,11):
    if i%2==1:
        sum = sum+i
print("홀수합계 :",sum)



# # for문
# # 구조 - for 변수 in 범위(range,list,문자열) :

# for i in range(10):
#     print(i)
    

# # 반갑습니다. 10번 출력하세요
# for i in range(10):
#     print("반갑습니다.")
    
# a_list = []
# sum = 0
# for i in range(10):
#     num = int(input("숫자를 입력하세요."))
#     if num%2==0:
#         break # 반복문을 중지시키는 명령어
#     # append
#     sum = sum+num
#     a_list.append(num)
    
# print("리스트 :",a_list)
# print("합계 :",sum)

