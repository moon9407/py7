# print("%d" % (100,200)) # 에러 : % 자리수(개수)와 뒤 개수가 맞아야한다.
# print("%d %d" % (100))  # 에러
#print("%d\t%d" % (100,200))# %자리와 뒤 개수가 일치

#str1 = "안녕"
#str2 = "국어"
#str3 = "영어"
#str4 = "수학"
#str5 = "합계"
#str6 = "평균"
#print(str1,str2,str3,str4)
# \t 탭키 적용, \n 줄바꿈.

# 입력부분
name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
total = kor+eng+math
avg = (kor+eng+math)/3

print("-"*50)
#print("%s\t%s\t%s\t%s\t%s\t%s" % (str1,str2,str3,str4,str5,str6))
print("%s\t%s\t%s\t%s\t%s\t%s" % ("이름","국어","영어","수학","합계","평균"))
print("-"*50)
#print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,math,kor+eng+math,(kor+eng+math)/3))
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,math,total,avg))
