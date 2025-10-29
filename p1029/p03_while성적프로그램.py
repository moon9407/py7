# while
stu_list = []
while True:
    print("[학생성적프로그램]")
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("3.학생성적수정")
    print("0.프로그램 종료")
    print("-"*20)
    no = int(input("원하는 번호를 입력하세요."))
    # no ==0 비교
    if no==0:
        break
    elif no==1:
        #학생성적입력
        print("[학생성적입력]")
        name = input("이름을 입력하세요.")
        kor = int(input("국어점수를 입력하세요."))
        eng = int(input("영어점수를 입력하세요."))
        math = int(input("수학점수를 입력하세요."))
        total = kor+eng+math
        avg = total/3
        stu_list.append([name,kor,eng,math,total,avg])
        print("이름 : {}".format(stu_list[0]))
        print("국어점수 : {}".format(stu_list[1]))
        print("영어점수 : {}".format(stu_list[2]))
        print("수학점수 : {}".format(stu_list[3]))
        print("합계 : {}".format(stu_list[4]))
        print("평균 : {:.2f}".format(stu_list[5]))
        print()
        print("이름\t국어\t영어\t수학\t합계\t평균\t")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(*stu_list))


# 5번 동안 숫자를 입력받아 합계를 출력하시오.
# for  변수 안받을때 _표시
# sum = 0
# for i in range(5):
#     i = int(input("숫자를 입력하세요.")) 
#     sum = sum+i
#     sum += i # 위와 같은 의미
#     print("입력숫자 :",i)
# print("총 합:{}".format(sum))

# while
# num = 0
# i = 1
# while i<5:
#     i = int(input("숫자를 입력하세요.")) 
#     sum += i
#     i += 1
# print("총 합:{}".format(num))




# # 1~10 까지의 합을 구하시오.
# #for
# sum = 0
# for i in range(1,11):
#     sum = sum+i
# print("총 합:{}".format(sum))

# #while
# num = 0
# i = 1
# while i<11:
#     num=num+i
#     i = i+1    # while은 증감식 무조건 추가
# print("총 합:{}".format(num))

