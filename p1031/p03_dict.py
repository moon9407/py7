# 딕셔너리 : 쌍 2개가 하나로 묶인구조
# stu_list = [name:'홍길동',kor:100,eng:100,math:100]
# stu_list = {키(key):값(value),키:값,키:값......}
# 다른 프로그래밍 언어에서는 해시(hash),연관배열(Associative Array)라고 함

# 딕셔너리 생성
# list1 = [1,2,3]
# dic1 = {1:'a',2:'b',3:'c'}
# dic1 = {"no":1,"name":"홍길동","class":3}

# print(list1)
# print(dic1)
# 리스트에 추가 = append,insert,extend

# stu = {"학번":1,"이름":"홍길동","학과":"컴퓨터공학"}
# print(stu)
# 딕셔너리 수정 - 없는 키값 입력하면 추가 됨.
# stu['연락처']='010-1111-1111'
# print(stu)
# 딕셔너리 수정 - 값에 그냥 넣으면 됨. 키는 수정 못함
# stu['이름']= '홍길자'
# print(stu)
# print(stu['성명']) # 없는 키 출력 시 에러
# stu['성명1']= '홍' # 딕셔너리 추가
# print(stu)
# 딕셔너리 삭제
# del(stu['성명1'])
# print(stu)

stu_list = [
    {"no":1,"name":"홍길동","kor":100}
]

print(stu_list[0]['no'])
print(stu_list[0]['name'])


a_dic = {"no":1,"name":"홍길동","kor":100}
print(a_dic['kor'])       # 없는 키 값 입력 시 에러

# 딕셔너리 .get()함수
print(a_dic.get('kor1'))   # 없는 키 값 입력 시 None타입으로 출력 됨. 

# 딕셔너리 keys()
print(a_dic.keys())
a_list = list(a_dic.keys())
print(a_list[0])

# 딕셔너리 values()
print(a_dic.values())
b_list = list(a_dic.values())
print(b_list[0])

# 딕셔너리 items() - key,value
print(a_dic.items()) 
c_list = list(a_dic.items())
print(c_list)

aa_list = [
    ['no',1],
    ['name','홍길동'],
    ['kor',100],
]

#홍길동
print(aa_list[1][1])
print(c_list[1][1])

# 키 존재 확인
stu_dic = {"no":1,"name":"홍길동","kor":100}
if 'eng' in stu_dic:
    print("키가 존재합니다.")
else:
    print("키가 존재하지않습니다.")
    
