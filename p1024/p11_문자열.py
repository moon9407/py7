# # 삼중따옴표는 있는 그대로 출력(안쓸때는 \ \n 추가)
# print("""abcde
#       fghij
#       klmno
#       pqrst
#     uvwxyz""")

# # 문자열
# str1 = "안녕"
# str2 = "안녕"
# print(str1)
# print(str1,str2)
# print(str1,"--",str2)
# # %출력 장점은 자리수지정, 빈공백에 0을 표시, 소수점 제한
# # %s 문자열, %d 정수, %f 실수
# print("%s -- %s"%(str1,str2))

# print("안녕"*10) # *문자열 반복(파이썬만 가능)
# print("-"*50)
# print("이름\t국어\t영어\t수학\t합계\t평균")

# # 문자열 선택 []
# name = "안녕하세요"
# print(name[0]) #안
# print(name[-5])#안 
# print(name[1]) #녕
# print(name[-4])#녕
# print(name[2]) #하
# print(name[-3])#하
# print(name[3]) #세
# print(name[-2])#세
# print(name[4]) #요
# print(name[-1])#요

# # 문자슬라이싱 (원하는 부분부터 글자 출력)  ex) 0:4면 0부터 시작해서 4전까지라는 뜻!
# print(name[0:2]) #안녕
# print(name[0:4]) #안녕하세
# print(name[2:4]) #하세
# print(name[2:])  #하세요   #뒷자리를 입력하지 않으면 마지막 까지 출력
# print(name[:3])  #안녕하   #앞자리를 입력하지 않으면 마지막 까지 출력

# # 문자 길이
# print(len(name)) #문자열의 길이(글자수) 출력

# # 슬라이싱 - 스텝 (원하는 글자만 출력)
# print(name[::2]) # 안하요  #모든 문자열 2칸씩 띄워 출력
# print(name[::-1]) # 요세하녕안  # 반대로 출력
# print(name[::3]) # 안세
# print(name[::1]) # 안녕하세요

# 880101-2111111 주민번호
# 1,3 - 남자, 2,4 - 여자
jumin = input("주민번호를 입력하세요.")
print(jumin[7])

if(int(jumin[7])%2=="0"):
    print("여자입니다.")
else:
    print("남자입니다.")

    