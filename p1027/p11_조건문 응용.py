# # 조건문 if (조건)
# a = 100
# if a>10: #True,False 2가지 bool(불)
#     print("참입니다.")

# a = 100
# if a>10:
#     print("참입니다.")
# else:
#     print("거짓입니다.")


# num = int(input("숫자를 입력하세요."))
# if num>0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")
    
# 입력한 숫자에 50을 더해서 100보다 큰수인지 출력하시오.
# 100보다 큰수입니다.
# 100보다 작은수입니다.

# a = int(input("숫자를 입력하세요."))

# # 방법 1
# a = a+50
# if a>100:
#     print("입력 값 :",a-50,"현재값 :",a,"100보다 큰 수입니다")
#     print("입력한 값 : %d, 현재 값 : %d, %s"% (a-50,a,"100보다 큰수입니다."))
# else:
#     print("입력 값 :",a,"현재값 :",a,"100보다 작은 수입니다.")
#     print("입력한 값 : %d, 현재 값 : %d, %s"% (a-50,a,"100보다 작은수입니다."))


# 방법2
# if (a+50)>100:
#     print("100보다 큰수입니다.")
    
# else:
#     print("100보다 작은수입니다.")

# 입력한 값이 짝수인지 홀수인지 출력하시오.
# num = int(input("숫자를 입력하세요."))

# if num % 2 == 0:
#     print("입력한 값 : %d, 결과 : %s"% (num, "짝수입니다."))
# else:
#     print("입력한 값 : %d, 결과 : %s"% (num, "홀수입니다."))


# 문자열 연산자
# 문자열 슬라이싱
str1= "안녕하세요"
# 안(0)녕(1)하(2)세(3)요(4)
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
# 안(-5)녕(-4)하(-3)세(-2)요(-1)
print(str1[-1])
print(str1[-2])
print(str1[-3])
print(str1[-4])
print(str1[-5])
# 1부터 3번 앞까지 
print(str1[1:3]) # 녕하
print(str1[1:4]) # 녕하세
# 입력이 없으면 시작부터or끝까지
print(str1[1:]) # 녕하세요
print(str1[:3]) # 안녕하
print(str1[:]) # 안녕하세요
# [처음번호:끝:스탭]
print(str1[::1]) #안녕하세요
print(str1[::-1]) #요녕하세안
print(str1[::2]) #안하요
print(str1[::-2]) #요하안
print(str1[1:4:2]) #녕세
print(str1[1:4:3]) #녕
a = "123456789"
print(a[::2])  # 홀수만
print(a[1::2]) # 짝수만
print(a[2::3]) # 3의 배수만

### 입력한 문자에 마지막 글자를 출력하시오.
# input1 = input("문자를 입력하세요")
# print("마지막 글자 :", input1[-1])

# 파일(확장자명)찾기
input1 = input("파일이름를 입력하세요")
print("마지막 글자 :", input1[-3:])

