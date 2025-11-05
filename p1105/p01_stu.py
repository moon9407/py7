stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0}
]
# dict 타입 -> 문자열로 변환
stu_str = ""
for i in range(len(stu_list)):
    stu_str += f"{stu_list[i]['stuno']},{stu_list[i]['name']},\
{stu_list[i]['kor']},{stu_list[i]['eng']},{stu_list[i]['math']},\
{stu_list[i]['total']},{stu_list[i]['avg']},{stu_list[i]['rank']}\n"

print(stu_str)

f = open("C:/down/aaa.txt","w") # 파일이 없으면 w모드는 파일을 생성 (새로할 때 마다 덮어쓰기)
stu_data = ""
f.write(stu_str)
f.close()

# 파일저장

# 파일 다시 읽어와서, dict타입으로 변경 후 출력
a_list = []
f = open("C:/down/aaa.txt","r")
while True:
    txt = f.readline()
    if txt == "" : break
    a_list.append(txt.strip().split(",")) # 리스트 추가
    
print(a_list)
f.close



# f = open("C:/down/aaa.txt","w")

# stu_str = f"{stu_list[0]['stuno']},{stu_list[0]['name']},\
# {stu_list[0]['kor']},{stu_list[0]['eng']},{stu_list[0]['math']},\
# {stu_list[0]['total']},{stu_list[0]['avg']},{stu_list[0]['rank']}\n"

# f.close()
# f = open("C:/down/aaa.txt","a")
# for i in range(2):
#     stu_str += f"{stu_list[i+1]['stuno']},{stu_list[i+1]['name']},\
# {stu_list[i+1]['kor']},{stu_list[i+1]['eng']},{stu_list[i+1]['math']},\
# {stu_list[i+1]['total']},{stu_list[i+1]['avg']},{stu_list[i+1]['rank']}\n"
# f.write(stu_str)

# print("완료")
# f.close()

# for stu in stu_list:
#     print(f"{stu['stuno']}\t{stu['name']}\t{stu['kor']}\t{stu['eng']}\t\
# {stu['math']}\t{stu['total']}\t{stu['avg']}\t{stu['rank']}\t")

