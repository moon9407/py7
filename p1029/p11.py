import random
# a_list = [9,1,2,5,6,8,3,4,7]
#                #enumerate는 인덱스 번호를 리턴해줌
# for i,val in enumerate(a_list):
#     print(val,end="\t")
#     if (i+1)%3 == 0:
#         print() 

a_list = list(range(1,17))
random.shuffle(a_list)
# print(a_list)
### 4*4 리스트 형태로 출력
for i ,val in enumerate(a_list):
    print(val,end="\t")
    if (i+1)%4==0:
        print()




# # 3*3 리스트 형태
# a_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# # [ [1,2,3],[4,5,6],[7,8,9]]
# for aa in a_list:   
#     for a in aa:
#         print(a,end="\t")
#     print()
        


# a_list = list(range(1,10))
# b_list = []
# # [
# #    [1,2,3],
# #    [4,5,6],
# #    [7,8,9]
# #]
# # 1 2 3
# # 4 5 6
# # 7 8 9
# 3*3 리스트형태
# # print(a_list)
# for i in (a_list):
#     print(i,end="\t")
#     if i%3==0:
#         print()
        
# 4*4 배열 리스트형태로 출력하시오
# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12
# 13 14 15 16
# a_list = list(range(1,17))

# for i in a_list:
#     print(i,end="\t")
#     if i%4==0:
#         print()
        
# b_list = list(range(1,26))
# print("-"*50)
# for i in b_list:
#     print(i,end="\t")
#     if  i%5==0:
#         print()



# # 리스트 자동으로 만드는법
# a_list = [1,2,3,4,5,6,7,8,9]
# print(a_list)
# b_list = list(range(1,10))   ##### 제일 중요
# print(b_list)
# c_list = [i for i in range(1,10)]
# print(c_list)

# d_list = ['0','0','0','0','0','0','0','0','0']
# print(d_list)
# e_list = list('0' * 9)       ##### 제일 중요
# print(e_list)
# f_list = ['0' for i in range(9)]  ##### 제일 중요
# print(f_list)

# c_list = list(range(1,32))
# d_list = ['일','월','화','수','목','금','토']
# print(d_list,end="\t")
# print()
# print("-"*50)
# for i in c_list:
#     print(i,end="\t")
#     if  i%7==0:
#         print()