# 변수 - 숫자(정수,실수), 문자열, 불(True,False)
# 리스트, 튜플, 셋
# 리스트 - 배열 : 데이터를 여러개 저장하는 공간
# 변수는 한개값만 저장가능하고 마지막게 선택됨
a = 10
a = 5
print(a)

fruit = ["사과","배","복숭아","딸기","포도"]
print(fruit[0]) #사과
print(fruit[1]) #배
print(fruit[2]) #복숭아
print(fruit[3]) #딸기
print(fruit[4]) #포도
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[0])
total = ["사과",1,2,True,1.25]
print(total)


#### 리스트 데이터 추가 - append, insert
# 리스트에 추가할 때 - .append() # 제일 뒤에 추가됨
stuscore = ['홍길동',100,100]
print(stuscore)
stuscore.append(100)
print(stuscore)

# 1번째 방(주소,인덱스)에 값 5를 추가
stuscore.insert(1,5)
print(stuscore)

#### 리스트 데이터 삭제 - pop, remove,del
#.pop() 은 제일 뒤에가 삭제
stuscore.pop()
print(stuscore)

#.remove는 해당 리스트 값 삭제
stuscore.remove("홍길동")
stuscore.remove(100)
print(stuscore)

# del 은 해당 번호를 삭제
del total[0]
print(total)

