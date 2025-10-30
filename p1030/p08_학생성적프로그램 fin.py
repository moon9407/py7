import random
stu_list = []
stu_count = 10101 # 학생번호
titles = ['번호','이름','국어','영어','수학','합계','평균']

# 학생성적프로그램
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
    
    if choice == 1:
        print("[학생성적입력]")
        name = input("{}번 학생이름을 입력하세요>>".format(stu_count))
        kor = int(input("국어점수를 입력하세요.>>"))
        eng = int(input("영어점수를 입력하세요.>>"))
        math = int(input("수학점수를 입력하세요.>>"))
        total = kor+eng+math
        avg = total/3
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        stu_count = stu_count+1            # 학생번호 1증가
        print("성적입력이 완료되었습니다.")
        print()
        
    elif choice == 2:
        print(" "*10,"[ 학생성적리스트 ]")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print("-"*50)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus))
        print()
            
    elif choice == 3:
        print("[ 학생성적수정 ]")
        for idx,stus in enumerate(stu_list):
            print("{}.{}{}".format(idx+1,stus[0],stus[1]))
        print("-"*50)
        choice = int(input("수정하려는 번호를 입력하세요.>>"))
        print(" {} 학생 수정과목 선택".format(stu_list[choice-1][1]))
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        
        sub = int(input("수정할 과목을 입력하세요."))
        print("-"*50)
        print("현재 {}점수 : {}".format(titles[sub+1],stu_list[choice-1][sub+1]))
        
        stu_c = int(input("수정할 점수를 입력하세요.>>"))
        stu_list[choice-1][sub+1] = stu_c
        stu_list[choice-1][5] = stu_list[choice-1][2]+stu_list[choice-1][3]+stu_list[choice-1][4]
        stu_list[choice-1][6] = stu_list[choice-1][5]/3
        
        print("{}점수 {}점으로 수정이 완료되었습니다.".format(titles[sub+1],stu_c))
        print()
        
    elif choice == 4:
        print("[학생성적삭제]")
        for idx,stus in enumerate(stu_list):
            print("{}.{}{}".format(idx+1,stus[0],stus[1]))
        print("-"*50)
        choice = int(input("삭제하려는 번호를 입력하세요.>>"))
        flag = int(input("{} {} 학생이 맞습니까? (1.yes, 2.no)").\
            format(stu_list[choice-1][0],stu_list[choice-1][1]))
        if flag == 2:
            print("삭제가 취소되었습니다.")
            continue
        
        del stu_list[choice-1]
        print("삭제가 되었습니다.")
        print(stu_list)
        
        
    elif choice == 0:
        print("[프로그램 종료]")     
        print()     
        break

