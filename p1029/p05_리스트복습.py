stu_list = []
# ['홍길동',100,90,80,270,90.00]


while True:
# 반복시작-----------------------
    name = input("이름을 입력하세요.")
    kor = int(input("국어점수를 입력하세요."))
    eng = int(input("영어점수를 입력하세요."))
    math = int(input("수학점수를 입력하세요."))
    total = kor+eng+math
    avg = total/3
    # stu_list.append(name)
    # stu_list.append(kor)
    # stu_list.append(eng)
    # stu_list.append(math)
    # stu_list.append(total)
    # stu_list.append(avg)
    stu_list = [name,kor,eng,math,total,avg]
    print("이름 : {}".format(stu_list[0]))
    print("국어점수 : {}".format(stu_list[1]))
    print("영어점수 : {}".format(stu_list[2]))
    print("수학점수 : {}".format(stu_list[3]))
    print("합계 : {}".format(stu_list[4]))
    print("평균 : {:.2f}".format(stu_list[5]))
    print()
    print("이름\t국어\t영어\t수학\t합계\t평균\t")
    print("-"*50)
    # print("{}\t{}\t{}\t{}\t{}\t{}\t".format(stu_list[0],stu_list[1],stu_list[2],stu_list[3],stu_list[4],stu_list[5]))
    # print()
    print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(*stu_list))