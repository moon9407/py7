import random
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00],
    [10102,'유관순',90,90,90,280,90.00],
    [10103,'이순신',100,100,100,300,100.00]
]
stu_count = 10104  #학생번호
titles = ['번호','이름','국어','영어','수학','합계','평균']


while True:
    print("-"*50)
    print(" "*10,"[ 학생성적프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-"*50)
    choice = int(input("원하는 번호를 입력하세요.>>"))

# 학생입력부분
    if choice == 1:
        print("1. 학생성적입력")
        name = input("이름을 입력하세요.")
        kor = int(input("국어 점수를 입력하세요."))
        eng = int(input("영어 점수를 입력하세요."))
        math = int(input("수학 점수를 입력하세요."))
        total = kor+eng+math
        avg = total/3
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        stu_count = stu_count+1
        print("성적 입력이 완료되었습니다.")
        

# 학생 출력부분
    elif choice == 2:
        print("2. 학생성적출력")
        print("-"*40)
        print(*titles,sep='\t')
        print("-"*40)
        for stu in stu_list:
            print(*stu,sep='\t')

    elif choice == 3:
        while True : 
            print("3. 학생성적수정")
            print("0. 이전단계")
            ("-"*40)
            
            for i,stus in enumerate(stu_list):
                print("{}.{} {}".format(i+1,stus[0],stus[1]))
            ("-"*40)
            
            ch = int(input("원하는 학생 번호를 입력하세요."))
            if ch>i+1:
                print("번호를 정확히 입력해주세요")
            elif ch==0:
                break    
            print("{} 학생 수정과목 선택".format(stu_list[ch-1][1]))
            print("1. 국어점수")
            print("2. 영어점수")
            print("3. 수학점수")
            
            sub = int(input("수정과목을 번호로 선택하세요."))
            print("*"*40)
            print("{}학생 {}점수 : {}".format\
                (stu_list[ch-1][1],titles[sub+1],stu_list[ch-1][sub+1]))
            
            num = int(input("수정할 {}점수를 입력하세요.>>".format(titles[sub+1])))
            stu_list[ch-1][sub+1] = num
            stu_list[ch-1][5] = stu_list[ch-1][2]+stu_list[ch-1][3]+stu_list[ch-1][4]
            stu_list[ch-1][6] = stu_list[ch-1][5]/3
            print("{}학생 {}점수 : {}점으로 수정되었습니다.".format(stu_list[ch-1][1],titles[sub+1],num))