a_list = [1,2,3,4,5,6,7,8,9]
print(a_list[1::2]) # 짝수만 출력
print(a_list[::2])  # 홀수만 출력
print(len(a_list))

a_list = [0,5,3,1,2,4,1,5,6]
a_list[0] = 100 # 값 변경 방법
print(a_list)

# 입력한 값이 홀수,짝수인지 출력하세요.
# if num%2==0:
a_list = [0,5,3,1,2,4,1,5,6]
# print(""%(a_list[0],))
# 0번째 : 0, 2번째 : 3
print("0번주소 : %d, 2번주소 : %d" % (a_list[0],a_list[2]))



# str1 = "안녕하세요"
# print(str1[1:4])
# print(str1[::-1]) # 역순 출력
# print(a_list[2:5:2]) # 리스트도 슬라이싱 가능



 
