# 숫자 2개를 입력받아 사칙연산 결과를 출력하시오.
# 10+5=15
# 10-5=5
# 10*5=50
# 10/5=2

num = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))

print("%d+%d=%d"% (num,num2,(num+num2)))
print("%d-%d=%d"% (num,num2,(num-num2)))
print("%d*%d=%d"% (num,num2,(num*num2)))
print("%d/%d=%d"% (num,num2,(num/num2)))

