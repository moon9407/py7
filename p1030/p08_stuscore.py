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
        
        
        print("성적입력이 완료되었습니다.")
        print()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 0:
        print("[프로그램 종료]")     
        print()     
        break

