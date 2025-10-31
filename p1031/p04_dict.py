# stu_dic = {}
# # no":1,"name":"홍길동","kor":100 딕셔너리에 추가 후 출력
# # 키 : 값 으로 모두 출력

# stu_dic["no"] = 1
# stu_dic["name"] = "홍길동"
# stu_dic["kor"] = 100

# print(stu_dic)

# for k,v in stu_dic.items():
#     print("{}:{}".format(k,v)) #("no,1")
    
# for k in stu_dic.keys():
#     print("{}:{}".format(k,stu_dic[k])) # "no" , stu_dic["no"]

# for v in stu_dic.values():
#     print("값 : {}".format(v))

stu_list = [
    {"no":1,"name":"홍길동","kor":100},
    {"no":2,"name":"유관순","kor":80},
    {"no":3,"name":"이순신","kor":90}
]

# 3번째에 있는 kor - 50 으로 변경하세요
# stu_list[2][2] = 50
stu_list[2]['kor'] = 50
print(stu_list)

stus = {"no":3,"name":"이순신","kor":90}
stus['kor'] = 50
print(stus)

a_list = [3,'이순신',90]
# 90 ->50
a_list[2]=50
print(a_list)

