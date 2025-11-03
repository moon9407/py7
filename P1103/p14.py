# 로또 맞추기 프로그램
# 로또 1개를 자동번호 추출로 입력받아,
# 몇개가 맞는지 출력하시오.
import random
# 로또 번호   
lotto = random.sample(range(1,46),6)
print('[ 로또 번호 ]')
print(lotto)
counts = []

# 자동추출 6개 my번호
my_lottos = []
for i in range(5):
    my_lottos.append(random.sample(range(1,46),6))
print("-"*50)
# 입력한 my숫자 번호
print('[ 나의 랜덤 로또 번호 ]')
for my_lotto in my_lottos:
    print(my_lotto)

# 번호비교함수
def cal():
    # print(lotto,my_lottos)
    for my_lotto in my_lottos: # 6개묶음 로또번호
        count = 0
        for i in my_lotto:     # 1개묶음 로또번호
            if i in lotto:     # 1개 번호가 로또번호에 있는지 확인
                count += 1
        counts.append(count)        


# 맞는 개수도 
cal()
print("-"*50)
print("[ 로또번호 맞춘 개수 ]")
print(counts)

# 3개 로또 자동 방법1
# def func():
#     num_list1 = random.sample(range(1,46),6)
#     num_list2 = random.sample(range(1,46),6)
#     num_list3 = random.sample(range(1,46),6)
#     return num_list1,num_list2,num_list3

# a_list = func()
# print(a_list)

   




