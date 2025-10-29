# 1~45까지 6개의 랜덤숫자를 출력하시오
# 중복은 안됨

# 1. 변수 선언
import random
a_list = [] # 내가 입력한 번호
count = 0 # 맞춘 갯수 -len(c_list)
c_list = [] # 맞춘 번호
lotto = random.sample(range(1,46),6)
lotto.sort() # 로또 번호 정렬

print(lotto) # 정답 확인용. 확인 후 삭제
# 2. 번호 입력
# 6개 숫자를 입력받아 출력하시오.
for i in range(6):
    m_num = int(input("숫자를 입력하세요."))
    a_list.append(m_num)
a_list.sort()

# 3. 맞춘 번호 확인
for i in lotto:
    for j in a_list:
        if i==j:
            count = count+1
            c_list.append(i)
            break # 가장 가까운 for문을 중지함.
c_list.sort()

# 4. 결과 확인
print("[ 결과화면 ]")

print("맞춘번호:",c_list)
print("정답개수:",count)


# 5. 당첨금 출력
# 0~1개- 0원 2개 - 5000원, 3개 - 50000원, 4개 - 100만원, 5개- 5000만원 6개 - 20억
if count<2:
    print("맞은개수:{}개, 당첨금 0원입니다.".format(count))
elif count==2:
    print("맞은개수:{}개, 당첨금 5000원입니다.".format(count)) 
elif count==3:
    print("맞은개수:{}개,당첨금 50000원입니다.".format(count))           
elif count==4:
    print("맞은개수:{}개, 당첨금 100만원입니다.".format(count))            
elif count==5:
    print("맞은개수:{}개, 당첨금 5000만원입니다.".format(count)) 
elif count==6:
    print("맞은개수:{}개, 당첨금 20억원입니다.".format(count)) 
            
