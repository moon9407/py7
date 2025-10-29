# 로또 번호 맞추기 프로그램
# 1. 변수선언, 번호생성
import random                             # 랜덤 선언
lotto = random.sample(range(1,46),6)      # 랜덤번호 출력
a_list = []                               # 입력한 번호 리스트
lotto.sort()                              # 로또 번호 정렬
count = 0                                 # 맞은 개수
c_list = []                               # 맞은 번호 리스트
l_list = [0,5000,50000,1000000,50000000,2000000000] # 당첨금액 리스트

print(lotto) #테스트용 랜덤출력번호 확인

# 2. 번호입력     
for i in range(6):           
    m_num = int(input("숫자를 입력하세요."))
    a_list.append(m_num)        # 입력한 숫자를 a_list(입력한 번호 리스트)에 추가
a_list.sort()                   # 리스트 낮은 수 부터 정렬

# 3. 당첨번호 확인
for i in lotto:                      # 두개가 맞는지 확인해야하니 중첩for문 사용
    for j in a_list:                   # 윗줄은 당첨번호, 해당 줄은 입력번호
        if i==j:                           
            count = count+1                # count(맞은개수) 0에서 맞았을 시 +1로 개수 증가 0->1  1->2 
            c_list.append(i)               # 후 c_list(맞은번호 리스트)에 i(맞은번호) 추가
            break                         # break 사용 안해도 되지만 사용 시 맞은 후 뒷번호 확인 안하기 때문에 작업속도 up
c_list.sort()                   # c_list(맞은 번호 리스트) 낮은 번호부터 정렬 
  
# 4. 결과화면 출력
print("[ 당첨 결과 ]")
print("당첨번호:",lotto)
print("맞춘 번호:",c_list)

# 5. 당첨금 확인
if count<2:                        # 2개부터가 당첨이니 2보다 낮으면 꽝
    print("맞은개수 :{}, 당첨금액 : {:,d}원".format(count,l_list[0]))
elif count==2:                     # 포맷(count,l_list[])      []필수
    print("맞은개수 :{}, 당첨금액 : {:,d}원".format(count,l_list[1]))
elif count==3:
    print("맞은개수 :{}, 당첨금액 : {:,d}원".format(count,l_list[2]))
elif count==4:
    print("맞은개수 :{}, 당첨금액 : {:,d}원".format(count,l_list[3]))
elif count==5:
    print("맞은개수 :{}, 당첨금액 : {:,d}원".format(count,l_list[4]))
elif count==6:
    print("맞은개수 :{}, 당첨금액 : {:,d}원".format(count,l_list[5]))
