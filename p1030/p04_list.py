# a_list = [1,2,3,4,5]
# b_list = list(range(1,6))
# c_list = [i for i in range(1,6)]
# print(a_list)
# print(b_list)
# print(c_list)

# 리스트 추가 - append, insert, extend
# 리스트 제거 - prp,del,remove,clear
# 리스트 수정 - a_list[index] = 값
# index : 해당 위치값 리턴, 해당 리스트 안에 값이 없으면 에러
# aa_list = [10,5,15,7,9]
# print(aa_list.index(10)) # .index() : 안에 들은 값의 위치를 찾아줌

# # 1.비교 
# print(aa_list)
# num = int(input("원하는 번호를 입력하세요."))
# for idx,aa in enumerate(aa_list):
#     if aa == num:
#         aa_list[idx] = "x"
# print(aa_list)

# 2.비교 
# print(aa_list)
# num = int(input("원하는 번호를 입력하세요."))
# if num in aa_list:
#     aa_list[aa_list.index(num)] = "x"

# print(aa_list)

# 5*5의 2차원형태 리스트를 생성
# 좌표만들기

a_list = list(range(1,26))    # 1.리스트 생성

while True:                          
    print("[좌표 맞추기 게임]")
    print("-"*50)
    for idx,a in enumerate(a_list):
        print(a,end="\t")
        if (idx+1)%5==0:
            print()
    print("-"*50)
    num = int(input("숫자를 입력하세요"))
    print
    if num in a_list:
        a_list[a_list.index(num)] = "x"
        print(a_list)







