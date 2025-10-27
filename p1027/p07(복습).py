# 숫자 2개를 입력받아 사칙연산 결과를 출력하시오.
# 10+5=15
# 10-5=5
# 10*5=50
# 10/5=2

# 방법 1
num = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))

print("%d+%d=%d"% (num,num2,num+num2))
print("%d-%d=%d"% (num,num2,num-num2))
print("%d*%d=%d"% (num,num2,num*num2))
print("%d/%d=%d"% (num,num2,num/num2))


# 방법 2
n1 = input("숫자를 입력하세요.")
n2 = input("숫자를 입력하세요.")

print("%d+%d=%d"% (int(n1),int(n2),int(n1)+int(n2)))
print("%d-%d=%d"% (int(n1),int(n2),int(n1)-int(n2)))
print("%d*%d=%d"% (int(n1),int(n2),int(n1)*int(n2)))
print("%d/%d=%d"% (int(n1),int(n2),int(n1)/int(n2)))


# 방법 3
n1 = input("숫자를 입력하세요.")
n2 = input("숫자를 입력하세요.")

print("%s+%s=%d"% (n1,n2,int(n1)+int(n2)))
print("%s-%s=%d"% (n1,n2,int(n1)-int(n2)))
print("%s*%s=%d"% (n1,n2,int(n1)*int(n2)))
print("%s/%s=%d"% (n1,n2,int(n1)/int(n2)))

#방법 4
num = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
print(num+num2)
print(num-num2)
print(num*num2)
print(num/num2)