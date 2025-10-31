a_list = [1,1,2,3,4,2,3,1,5,4]
a_dic = {}
for i in a_list:
    if i not in a_dic:
        a_dic[i] = 1
    else:
        a_dic[i] += 1
        
print(a_dic)
        









# a_dic['홍길동'] = 100
# print(a_dic)

# b_dic = {}
# b_dic[1] = 1
# b_dic[2] = 1
# b_dic[1] = 10
# print(b_dic)

# for i in a_list:
#     a_dic[i] = 0
    
# print(a_dic)



# b_dic = {}
# # 딕셔너리 추가
# b_dic["홍길동"] = 100  # 없는 키 입력 시 추가
# b_dic["홍길동"] = 50   # 있는 키 입력 시 수정
