a_list = [1,2,3]
# list추가 = append,insert,extend
# append - 뒤에 추가
# 복합변수의 값이 변경됨.
a_list.append(10)
print(a_list)
# insert - (위치,값) 원하는 위치에 값 추가 가능
a_list.insert(1,200)
print(a_list)
a2_list = [5,6,7]
# extend는 리스트 2개를 합침
a_list.extend(a2_list)
print(a_list)

a_list = a_list + [10,20,30]
print(a_list)
# list 값 변경 - 위치값
a_list[2] = 1000
# a_list[100] = 1000 # 없는 주소를 넣으면 에러
print(a_list)

# 삭제 - pop() : 제일 뒤 삭제, del : 해당 위치 삭제, remove : 해당 값 삭제, clear : 모두 삭제
aa_list = [1,2,3,4,5,6,7]
aa_list.pop()  # 제일 뒤 삭제
print(aa_list)
del aa_list[0] # 해당 위치 삭제
print(aa_list) 
aa_list.remove(5) # 해당 값 삭제, 같은 값이 있을 경우 앞에서부터 하나만 삭제
print(aa_list)
aa_list.clear() # 리스트 값 전체 삭제
print(aa_list)


#비파괴적
a = 10
a + 100
print(a) # 10



# [] 1개 : 1차원 리스트
# [[]] 2개 : 2차원 리스트
# [[[]]] 3개 : 3차원 리스트

b_list = [
    ["홍길동",100,[1,2,3]],["유관순",99],["이순신",80],["김구",89]
]

print(b_list[0]) # 홍길동,100
print(b_list[0][0]) # 홍길동
print(b_list[0][2][1]) # 2
