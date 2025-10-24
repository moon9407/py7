# 이름 입력 - str %s
# 국어점수 입력 - int
# 영어점수 입력 - int
# 수학점수 입력 - int
# 합계 - int %d
# 평균 - float %f

# %print로 출력

name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
total = kor+eng+math
avg = total/3
#print("%s\t%d\t%d\t%d\t%d\t%f" % (name,kor,eng,math,total,avg)) #\t는 자동 공백, \n은 줄바꿈
print("이름 : %s" % name)
print("합계 : %d" % total)
print("평균 : %d" % avg)
