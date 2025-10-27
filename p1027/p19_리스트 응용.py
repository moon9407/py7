#이름, 국어,영어,수학,합계,평균
# 3명의 학생성적을 입력받아 저장해서 출력하시오.
# stus = []

# # 방법 1
# name = input("이름을 입력하세요.")
# kor = int(input("국어점수를 입력하세요."))
# eng = int(input("영어점수를 입력하세요."))
# math = int(input("수학점수를 입력하세요."))
# total = kor+eng+math
# avg = total/3
# stu_data = [name,kor,eng,math,total,"%.2f" % avg]
# stus.append(stu_data)
# print(stu_data)

# name2 = input("이름을 입력하세요.")
# kor2 = int(input("국어점수를 입력하세요."))
# eng2 = int(input("영어점수를 입력하세요."))
# math2 = int(input("수학점수를 입력하세요."))
# total2 = kor+eng+math
# avg2 = total/3
# stu_data2 = [name2,kor2,eng2,math2,total2,"%.2f" % avg2]
# stus.append(stu_data2)
# print(stu_data2)

# name3 = input("이름을 입력하세요.")
# kor3 = int(input("국어점수를 입력하세요."))
# eng3 = int(input("영어점수를 입력하세요."))
# math3 = int(input("수학점수를 입력하세요."))
# total3 = kor+eng+math
# avg3 = total/3
# stu_data3 = [name3,kor3,eng3,math3,total3,"%.2f" % avg3]
# stus.append(stu_data3)
# print(stu_data3)
# print(stus)


# 방법 2 정석
stus = []
#학생1
stu = []
name = input("이름을 입력하세요.")
stu.append(name)
kor = int(input("국어점수를 입력하세요."))
stu.append(kor)
eng = int(input("영어점수를 입력하세요."))
stu.append(eng)
math = int(input("수학점수를 입력하세요."))
stu.append(math)
total = kor+eng+math
stu.append(total)
avg = total/3
stu.append(avg)
print(stu)
stus.append(stu)

#학생2
stu = []
name = input("이름을 입력하세요.")
stu.append(name)
kor = int(input("국어점수를 입력하세요."))
stu.append(kor)
eng = int(input("영어점수를 입력하세요."))
stu.append(eng)
math = int(input("수학점수를 입력하세요."))
stu.append(math)
total = kor+eng+math
stu.append(total)
avg = total/3
stu.append(avg)
print(stu)
stus.append(stu)

#학생3
stu = []
name = input("이름을 입력하세요.")
stu.append(name)
kor = int(input("국어점수를 입력하세요."))
stu.append(kor)
eng = int(input("영어점수를 입력하세요."))
stu.append(eng)
math = int(input("수학점수를 입력하세요."))
stu.append(math)
total = kor+eng+math
stu.append(total)
avg = total/3
stu.append(avg)
stus.append(stu)
print(stu)
print(stus)

print(stus[0]) #['홍길동', 100, 99, 100, 299, 99.66666666666667]
print(stus[0]) #홍길동
print(stus[0]) #100
print(stus[1]) #['이순신', 100, 97, 89, 286, 95.33333333333333]