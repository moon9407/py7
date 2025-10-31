# 학생성적 입력,출력, 수정,삭제를 구현하시오.
import random
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00],
    [10102,'유관순',90,90,90,280,90.00],
    [10103,'이순신',100,100,100,300,100.00]
]
stu_count = 10104  #학생번호
titles = ['번호','이름','국어','영어','수학','합계','평균']

while True:
    print("-"*40)
    print("        [ 학생성적 프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램 종료")
    print("-"*40)
    
    put = int(input("원하는 항목을 선택하세요.>>"))
    
    if put > 4:
        print("번호를 정확히 입력해주시기 바랍니다.")
    
    elif put == 1:
        print("[1. 학생성적입력]")
        name = input("{}번 학생 이름을 입력하세요.>>".format(stu_count))
        kor = int(input("국어점수를 입력하세요.>>"))
        eng = int(input("영어점수를 입력하세요.>>"))
        math = int(input("수학점수를 입력하세요.>>"))
        total = kor+eng+math
        avg = total/3
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        stu_count = stu_count+1
        print("{}학생 입력이 완료되었습니다.".format(name))
        print()
            
        
    elif put == 2:
        print("[2. 학생성적출력]")
        ("-"*40)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        ("-"*40)
        for stu in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stu))
        print()
        
        
    elif put == 3:
        while True:
            print("[3. 학생성적수정]")
            print("0.이전단계")
            for i,stu in enumerate(stu_list):
                print("{}.{}\t{}".format(i+1,stu[0],stu[1]))
                
            print("-"*40)
            ch = int(input("수정하려는 학생번호를 입력하세요.>>"))
            if ch > i+1:
                print("번호를 정확히 입력해주시기 바랍니다.")
                continue
            elif ch == 0:
                break
            print("{}학생 수정과목 선택".format(stu_list[ch-1][1]))
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
            
        
    elif put == 4:
        print("[4. 학생성적삭제]")
        while True:
            print("0. 이전단계")
            for i,stu in enumerate(stu_list):
                print("{}.{}{}".format(i+1,stu[0],stu[1]))
            print("-"*40)
            
            num1 =  int(input("삭제하려는 학생 번호를 입력하세요.>>"))
            if num1 > i+1 :
                print("번호를 정확히 입력하세요.")
                continue
            elif num1 == 0:
                break
            num2 =  int(input("{}학생을 정말 삭제하시겠습니까? (1:yes,2:no)"))
            if num2 == 2:
                print("취소되었습니다.")
                continue
            
            del stu_list[num1-1]
            print("삭제되었습니다.")
            print()
        
        
        
    elif put == 0:
        end =  int(input("정말 종료하시겠습니까? (1:yes,2:no)"))
        if end == 2:
            print("취소되었습니다.")
            print()
            continue
        
        print("프로그램이 종료되었습니다.")
        print()
        break
            