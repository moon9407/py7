# year = 2025
# month = 10
# day = 28
# # 2025년 10월
# print("%d년 %d월 %d일" % (year,month,day))

### format() 함수  
# {1:5d} 1번주소 5자리 표현
# date1 = "{:d}년 {:d}월 {:d}일".format(year,month,day) # :d,:f,:s 생략 가능
# print(date1)

# a = 10000000
# a_format = "{}".format(a)
# a_format1 = "{:10d}".format(a)
# a_format2 = "{:010d}".format(a)
# a_format2 = "{:010,d}".format(a) # 쉼표 넣을 시 1000단위 표시 가능
# print(a_format)
# print(a_format1)
# print(a_format2)

# b = 25.2345678

# print("{:.2f".format(format))
# print("%.2f % b") # 위와 같지만 위가 더 좋기때문에 퍼센트는 굳이 사용 안해도 됌

# # list 타입 format함수 사용
# stus = ['홍길동',100,90,80]
# print("이름 :{},국어 : {},영어 :{},수학 : {}".format\
#     (stus[0],stus[1],stus[2],stus[3]))
# # *stus -> 전개연산자 stus[0],stus[1],stus[2],stus[3] 를 알아서 분리해줌(파이썬만 가능)
# print("이름:{},국어:{},영어:{},수학:{}".format(*stus))

# ### 
# bank = [1,'홍길동',100000]
# # 1번 홍길동 100,000원 으로 출력
# # 방법1
# print("{}번,{},{:,d}원".format(*bank))
# # 방법2
# print("{}번,{},{:,d}원".format(bank[0],bank[1],bank[2]))

name = "유관순"
rank = "3"
result = 98.234567
## 이름 : 유관순, 단계 : 3, 성공률 : 98.23%
a_list = [name,rank,result]
print("이름 : {}, 단계 : {}, 성공률 : {:.2f}%".format(*a_list))
## f함수 (변수로만 했을때 유리)
print(f"이름 : {name}, 단계 : {rank}, 성공률 : {result:.2f}%")
print(f"이름 : {a_list[0]}, 단계 : {a_list[1]}, 성공률 : {a_list[2]:.2f}%")




# % print
# a = 10
# print("%d"% a) # 10
# print("%5d"% a) #    10
# print("%05d"% a) # 00010

# b = 10.2345678
# print("%f" % b)
# print("%.2f" % b)
# print("%7.2f" % b)
# print("%07.2f" % b)

