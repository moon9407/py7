import random  #   선언, random 클래스 가져와서 쓰겠다.
print(random.random()) # 0.000000000000 <= x <1.000000000 사이의 난수를 랜덤으로 리턴.

# 아래부터는 파이썬만 있음
print(random.randrange(1,11)) # 1~10 사이의 숫자를 랜덤으로 리턴.
print(random.randint(1,11)) # 1~10 사이의 숫자를 랜덤으로 리턴.
print(random.sample([1,2,3,4,5],2)) # 해당 리스트에서 2개를 랜덤으로 가져옴.  단 중복이 안됨.
print(random.choices([1,2,3,4,5],k=4)) # 해당 리스트에서 4개를 랜덤으로 가져옴. 중복 가능.

a_list = [1,2,3,4,5]
random.shuffle(a_list) # 해당 리스트 순서를 섞음.
print(a_list)
