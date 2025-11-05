# 파일을 읽어오기

stu_list = []

f = open("C:/down/aaa.txt","r")
while True:
    txt = f.readline()
    if txt == "": break
    t_list = txt.strip().split(",")   # split은 쉼표를 기준으로 나눔

    
    # # 딕셔너리 형태 변경
    t_dic = {'stuno':int(t_list[0]),'name':t_list[1],'kor':int(t_list[2]),\
        'eng':int(t_list[3]),'math':int(t_list[4]),'total':int(t_list[5]),
        'avg':int(t_list[2]),'rank':int(t_list[7])
    }
    stu_list.append(t_dic)
print(stu_list)

#파일 -> 리스트[딕셔너리타입] -> 파일
stu_str = ""
for i in range(len(stu_list)):
    stu_str += f"{stu_list[i]['stuno']},{stu_list[i]['name']},{stu_list[i]['kor']},\
{stu_list[i]['eng']},{stu_list[i]['math']},{stu_list[i]['total']},\
{stu_list[i]['avg']},{stu_list[i]['rank']}\n"

print(stu_str)


f = open("C:/down/aaa.txt","w")
f.write(stu_str)
f.close()

print("완료")
