# 국어,영어, 수학접수를 입력받아 합계,평균을 출력하시오.
# 합계 : 299
# 평균 : 99.67 소수점 2자리 출력

# kor = int(input("국어점수를 입력하세요."))
# eng = int(input("영어점수를 입력하세요."))
# math = int(input("수학점수를 입력하세요."))
# total= kor+eng+math
# avg = (kor+eng+math)/3

# # 방법1
# print("합계 : %d 점"% total)
# print("평균 : %.2f 점"% avg)

# # 방법2
# print("합계 : %d 점"% (kor+eng+math))
# print("평균 : %.2f 점"% ((kor+eng+math)/3))

# # 방법3
# kor = input("국어점수를 입력하세요.")
# eng = input("영어점수를 입력하세요.")
# math = input("수학점수를 입력하세요.")

# print("합계 : %d 점"% (int(kor)+int(eng)+int(math)))
# print("평균 : %.2f 점"% ((int(kor)+int(eng)+int(math))/3))

# \t : 탭키- 사이 띄움, \n : 줄바꿈
# print("안녕\t하\n세요.")
name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
total= kor+eng+math
avg = (kor+eng+math)/3

name2 = input("이름을 입력하세요.")
kor2 = int(input("국어점수를 입력하세요."))
eng2 = int(input("영어점수를 입력하세요."))
math2 = int(input("수학점수를 입력하세요."))

name3 = input("이름을 입력하세요.")
kor3 = int(input("국어점수를 입력하세요."))
eng3 = int(input("영어점수를 입력하세요."))
math3 = int(input("수학점수를 입력하세요."))


print()
print()
print(" "*15+"학생성적프로그램")
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
# print("%s\t%d\t%d\t%d\t%d\t%.2f"% (name,kor,eng,math,total,avg))  #방법 1
print("%s\t%d\t%d\t%d\t%d\t%.2f"% (name,kor,eng,math,(kor+eng+math),((kor+eng+math)/3))) # 방법 2
print("%s\t%d\t%d\t%d\t%d\t%.2f"% (name2,kor2,eng2,math2,(kor2+eng2+math2),((kor2+eng2+math2)/3)))
print("%s\t%d\t%d\t%d\t%d\t%.2f"% (name3,kor3,eng3,math3,(kor3+eng3+math3),((kor3+eng3+math3)/3)))
print()
print()