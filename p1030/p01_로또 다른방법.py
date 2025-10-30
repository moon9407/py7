# 로또 맞추기 프로그램을 구현하시오.
# 1. 변수선언
import random
a_list = []
count = 0
c_list = []
l_list = [0,5000,50000,1000000,50000000,2000000000]
lotto = 0

# 2. 6개 번호 생성
lotto = random.sample(range(1,46),6)

lotto.sort()

print("당첨번호:{}".format(lotto))
# 3. 6개 번호입력
i =0
while i <6: # while을 쓰면 정확한 숫자를 원하는만큼만 넣을 수 있음
    m_num = input("{}번째 로또번호를 입력하세요.".format(i+1))
    if not m_num.isdigit(): # 문자열이 숫자인지 아닌지 확인해주는 함수
        print("숫자만 입력해주세요.")
        continue
    
    m_num = int(m_num)
    if 1<= m_num <=45:
        a_list.append(m_num)
        i = i+1
    else:
        print("1~45번까지의 번호를 입력해야합니다.")

a_list.sort()

# 4. 맞춘 번호확인
for i in lotto:        
    for j in a_list:
        if i==j:
            c_list.append(i)
            count = count+1
            break
# 파이썬에서만 사용가능 코드 
# for i in a_list:
#     if i in lotto:
#         c_list.append(j)
#         count = count+1
#         

c_list.sort()

# 5. 번호 출력
print("[당첨결과]")
print("당첨번호:{}".format(lotto))
print("입력번호:{}".format(a_list))
print("맞춘번호:{}".format(c_list))
print("-"*50)

# 6. 당첨금 출력
if count<2:
    print("맞춘갯수:{}, 당첨금액:{:,d}원".format(count,l_list[0]))
elif count==2:
    print("맞춘갯수:{}, 당첨금액:{:,d}원".format(count,l_list[1]))
elif count==3:
    print("맞춘갯수:{}, 당첨금액:{:,d}원".format(count,l_list[2]))
elif count==4:
    print("맞춘갯수:{}, 당첨금액:{:,d}원".format(count,l_list[3]))
elif count==5:
    print("맞춘갯수:{}, 당첨금액:{:,d}원".format(count,l_list[4]))
elif count==6:
    print("맞춘갯수:{}, 당첨금액:{:,d}원".format(count,l_list[5]))
    