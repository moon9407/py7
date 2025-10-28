# 이름  국어, 영어, 수학 점수를 입력받아
# 홍길동, 국어, 영어, 수학, 합계, 평균
a_list = ['홍길동',100,90,80,270,90.0000000]
# 이름 : 홍길동 국어 : 100점
print("이름:{} 국어:{}점 영어:{}점 수학:{}점 합계:{}점 평균:{:.2f}점".format\
      (a_list[0],a_list[1],a_list[2],a_list[3],a_list[4],a_list[5],))

print("이름:{} 국어:{}점 영어:{}점 수학:{}점 합계:{}점\
    평균:{:.2f}점".format(*a_list))

a = 10
b = 20

print("1번째값:{}\n2번째값:{}".format(a,b))
print("1번째값:{1:}\n2번째값:{0:}".format(a,b))
print("1번째값:{}\n2번째값:{}".format(b,a))
print(f"1번째값:{a}\n2번째값:{b}")





# 3개의 값을 입력받아, 숫자를 모두 합친 금액을 출력하시오.
# 금액 : 1,000,000원
# 1000원 이상 입력하세요.
# n1 = int(input("금액을 입력하세요."))
# n2 = int(input("금액을 입력하세요."))
# n3 = int(input("금액을 입력하세요."))
# total = n1+n2+n3
# print("총금액 : {:,d}".format(total))
# print("1번금액 : {:d}원\n2번금액 : {:d}원\n3번금액 : {:d}원\n총금액 : {:,d}".format(n1,n2,n3,total))
# print(f"1번금액 : {n1}원,2번금액 : {n2}원,3번금액 : {n3}원, \
#    \n 총금액 : {n1+n2+n3}원")


# n_format = "{:,d}".format(n1+n2+n3)
# print(f"1번금액 : {n1}원,2번금액 : {n2}원,3번금액 : {n3}원, \
#    \n 총금액 : {n1+n2+n3}원")
# print("총 금액",n_format,"원")


# year = 2025
# month = 10
# day = 28
# print("%d년 %d월 %02d일" % (year,month,day))
# day_format = "{}년 {}월 {}일".format(year,month,day)
# print(day_format)


