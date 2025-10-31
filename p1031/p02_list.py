stu_list = [
    # 이름,합계,등수
    ['홍길동',288,0],
    ['유관순',299,0],
    ['이순신',300,0],
    ['김구',295,0],
    ['강감찬',298,0]
]

for i in stu_list:
    r_count = 1 # 등수카운트
    for j in stu_list:
        if i[1]<j[1]:
            r_count = r_count+1
    # 비교가 완료되는 시점
    i[2] = r_count

print(stu_list)

for i,stu in enumerate(stu_list):
    for st in stu:
        if 



# 복합변수
# a = 10
# aa= a
# b = [1,2,3,4]
# bbb = b              # 얕은복사 : b를 그대로 복사 bbb에서 사용되면 b에서도 사용 됨
# bb= b[:] # 1,2,3,4   # 깊은복사 : b의 리스트 값은 가져오지만 사실상 새로 만든다는 의미 
# ccc = [*b]
# bb = [1,2,3,4] # 윗칸과 동일
# bb[0] = 100
# print(a)
# print(b)

# 단일변수, 단순변수
# a = 10  # q변수 -> 1개 값만 저장가능
# b= a    
# b= 20
# print(a)
# print(b)

