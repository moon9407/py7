# 국어,영어,수학 점수를 입력받아 합계와 평균을 출력하시오.
#num = int(input("국어점수를 입력하세요."))
#num2 = int(input("영어점수를 입력하세요."))
#num3 = int(input("수학점수를 입력하세요."))

#print("합계 : ",num+num2+num3)    # 쉼표구분자를 사용하면 타입이 달라진다.
#print("평균 : ",(num+num2+num3)/3)

kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
#avg = kor+eng+math
print("합계 : ",kor+eng+math)
print("평균 : ",(kor+eng+math)/3)
#print("평균 :",avg/3)100
print("평균 : %.2f" % ((kor+eng+math)/3)) #소수점 2째까지 나타낼때
