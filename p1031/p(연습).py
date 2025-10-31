import random
# 1. 로또 번호 생성
lotto = random.sample(range(1,46),6)
lotto.sort()
count = 0
c_list = []
l_list = [0,5000,50000,1000000,50000000,2000000000]
print(lotto)

# 2. 변수 지정
a_list = []

# 3. 번호입력
for i in range(6):
    num = int(input("로또 번호를 입력하세요.>>"))
    a_list.append(num)
print(a_list)

# 3. 번호 맞추기
for i in lotto:
    for j in a_list:
        if i==j:
            count = count+1
            c_list.append(i)
            
# 4 .결과
if count <2:
    print("당첨번호 : {}\n입력번호 : {}\n맞은개수 : {}\n맞은번호: {}\n당첨금 : {:,d}원"\
    .format(lotto,a_list,count,c_list,l_list[0]))
elif count ==2:
    print("당첨번호 : {}\n입력번호 : {}\n맞은개수 : {}\n맞은번호: {}\n당첨금 : {:,d}원"\
    .format(lotto,a_list,count,c_list,l_list[1]))
elif count ==3:
    print("당첨번호 : {}\n입력번호 : {}\n맞은개수 : {}\n맞은번호: {}\n당첨금 : {:,d}원"\
    .format(lotto,a_list,count,c_list,l_list[2]))
elif count ==4:
    print("당첨번호 : {}\n입력번호 : {}\n맞은개수 : {}\n맞은번호: {}\n당첨금 : {:,d}원"\
    .format(lotto,a_list,count,c_list,l_list[3]))
elif count ==5:
    print("당첨번호 : {}\n입력번호 : {}\n맞은개수 : {}\n맞은번호: {}\n당첨금 : {:,d}원"\
    .format(lotto,a_list,count,c_list,l_list[4]))
elif count ==6:
    print("당첨번호 : {}\n입력번호 : {}\n맞은개수 : {}\n맞은번호: {}\n당첨금 : {:,d}원"\
    .format(lotto,a_list,count,c_list,l_list[5]))
