import random

a_list= []
count = 0
c_list = []
l_list = [0,5000,50000,1000000,50000000,2000000000]

lotto = random.sample(range(1,46),6)
lotto.sort()

print(lotto)

for i in range(6):
    num=int(input("숫자를 입력하세요"))
    a_list.append(num)
    
print(a_list)

for i in lotto:
    for j in a_list:
        if i==j:
            count = count+1
            c_list.append(i)
            
print("[당첨결과]")
print("      [당첨번호]\n{}".format(c_list))

if count < 2:
    print("맞춘갯수 : {} 당첨금 {:,d}원".format(count,l_list[0]))
