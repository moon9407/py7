# if에 괄호는 안넣어도 무방, 끝에 세미콜론(:)은 넣어줘야함
# 엔터 후 들여쓰기(빈칸)는 꼭 들어가야함
# if (10>5):
#     print("정상입니다.")
# else:
#     print("비정상입니다.")

# 숫자를 입력받아 100보다 큰수인지 아닌지 출력하시오.
# 100보다 큰수입니다. 100보다 작은수입니다.

# num = int(input("숫자를 입력해주세요."))

# if (num>100):
#     print("100보다 큰수입니다")
# else:
#     print("100보다 작은수입니다")
    
# 입력된 숫자가 짝수인지 홀수인지 출력하시오.
# 짝수입니다. 홀수입니다.
# num = int(input("숫자를 입력해주세요."))

# if (num%2 == 0):
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

# 내부(내장)모듈 -외워두기
# 컴퓨터에 적용된 현재시간 가져오기
import datetime
now= datetime.datetime.now()
print(now) #시간 전체 출력
print(now.year,"년도")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

# 입력한 주민번호의 월을 파악해서 같은 현재 날짜와 같은 월이면
# 이벤트 대상입니다., 이벤트 대상이 아닙니다. 출력하시오.
jumin = input("주민번호를 입력하세요.")
#880101-1111111
if (int(jumin[2:4])==now.month):
    print("이벤트 대상입니다.")
else:
    print("이벤트 대상이 아닙니다.")


# n = "03"
# print(int(n))
# n2 = 3
# print("%02d" % n2)