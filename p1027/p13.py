#990101-1111111
#870101-2111111


#070101-3111111
#1,2
#주민번호를 입력받아, 남자인지 여자인지 출력하시오.
# 같은 달일 경우 이벤트 대상자입니다.
import datetime
now = datetime.datetime.now()
month = now.month

jumin = input("주민번호를 입력하세요")
a1 = jumin[7]
a2 = int(a1)

mth = jumin[2:4]
mth1 = int(mth)

if a2==1 or a2==3:
    print("남자입니다.")
else:
    print("여자입니다.")
    
if mth1== month:
    print("이벤트 대상자입니다.")
else:
    print("이벤트 대상자가 아닙니다.")
    