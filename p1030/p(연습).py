import random

a_list=[]
count=0
c_list =[]


lotto = random.sample(range(1,46),6)
lotto.sort()

print(lotto)

for i in range(6):
    num = int(input("숫자를 입력하세요."))
    a_list.append(num)

a_list.sort()
print(a_list)

for i in lotto:
    for j in a_list:
        if i==j:
            count = count+1
            c_list.append(i)
            break
        
print(c_list)

        

