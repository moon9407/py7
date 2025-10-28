# for 변수 in 범위:
# for i in range(5): #[0,1,2,3,4]
#     print(i,end=" ") # ,end="" 는 옆으로 출력
    
# 1~100까지 합을 구하시오.
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print("합계 :",sum)

# 10을 넘는 위치는 얼마를 더할때 일까요?
# 1+2+3+4+5+6+7+8+9+10+11+12+13+14

# sum = 0
# for i in range(1,101):
#     sum = sum+i
#     print(i,sum)
#     if sum>=100:
#         break
# print(f"{i}번째 :{sum}")


# 1*2*3*4*...*10 결과값을 출력하시오

result = 1
for i in range(1,11):
    result = result*i
print("결과 :",result)

# 100을 넘는 시점

result = 1
for i in range(1,11):
    result = result*i
    print(i,result)
    if result>100:
        break
    
print(f"{i}번째 : {result}")

