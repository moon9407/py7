stu_list = [
    ['홍길동',80,80,80,270,90.00],
    ['유관순',90,90,90,280,90.00],
    ['이순신',100,100,100,300,100.00]
]

titles = ['이름','국어','영어','수학','합계','평균']

while True:
    print("[ 학생성적수정 ]")
    print("1. 홍길동")
    print("2. 유관순")
    print("3. 이순신")
    print("-"*30)
    # 수정할 대상 선정
    num = int(input("수정하려는 학생 번호를 입력하세요.>>"))-1
    print("[ {} 학생 선택]".format(stu_list[num][0]))
    print("1. 국어성적수정")
    print("2. 영어성적수정")
    print("3. 수학성적수정")
    
    print("-"*30)
    subject = int(input("수정할 과목을 선택하세요.>>"))

    print("[ {} 학생 {}점수 수정]".format(stu_list[num][0],titles[subject]))
    print("현재 {} 점수 :{}".format(titles[subject],stu_list[num][subject]))
    # 국어점수 입력
    score = int(input("수정할 {}점수를 입력하세요.>>".format(titles[subject])))
    stu_list[num][subject] = score # 점수 변경
    stu_list[num][4] = stu_list[num][1]+stu_list[num][2]+stu_list[num][3]
    stu_list[num][5] = stu_list[num][4]/3
    print(stu_list)
print("프로그램 종료")   



# 0. 홍길동
# 1. 유관순
# 2. 이순신
# ---------
# 수정하고 싶은 학생 번호를 입력하세요.
# 국어점수 변경

# print('''\
#     [ 수정 할 학생 번호 ]
#     0. 홍길동
#     1. 유관순
#     2. 이순신
#     '''
# )
# num = int(input("수정 할 학생 번호를 입력하세요.>>"))
# # 1.번 선택
# # 국어점수를 70점으로 변경하고, 합계와 평균도 같이 변경해서 출력
# if num == 1:
#     print(stu_list[1])
#     a = int(input("수정할 점수를 입력하세요."))
#     stu_list[1][1] = a
#     stu_list[1][4] = stu_list[1][1]+stu_list[1][2]+stu_list[1][3]
#     stu_list[1][5] = stu_list[1][4]/3
    
# print("수정 후\n 이름:{} 국어점수:{} 영어점수:{} 수학점수:{} 합계:{} 평균:{:.2f}"\
#     .format(stu_list[1][0],stu_list[1][1],stu_list[1][2],stu_list[1][3],stu_list[1][4],stu_list[1][5]))

#______________________________________________________________________

# stu_list[2][2] = 70
# stu_list[2][4] = stu_list[2][1]+stu_list[2][2]+stu_list[2][3]
# stu_list[2][5] = stu_list[2][4]/3

# print(stu_list)




# print(stu_list[1][3])
# print(stu_list[2][0])
# stu_list[2][2] = 80
# print(stu_list[2][2])

 
 

# a_list = [1,2,3,4,5,6,7,8,9]    # len(a_list) : 9
# b_list = [                      # len(b_list) : 3
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# a_list[3] = 100
# print(a_list)

# b_list[2][1] = 50
# print(b_list)


# 1차원 리스트 출력
# for a in a_list:
#     print(a,end="\t")
# print()
# print("-"*50)
# for bs in b_list:
#     for b in bs:
#         print(b,end="\t")

    

