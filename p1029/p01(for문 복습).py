# for 변수 in 범위:

# for i in range(10):
#     pass # 아무것도 일어나지 않음 - 아무것도 넣지않으면 오류남
#     print("프로그램 종료")
#     break # 이 시점에서 반복문 종료

# for i in range(10):
#     if i%2==0:
#         print("프로그램 종료")
#         continue # 1회만 제외?



# for i in range(2,10): # 8번 실행
#     for j in range(1,10): # 9번 실행
#         print("숫자 :",j) # 1-72
#     print("-"*50) 
    

# for i in range(2,10):
#     print(i)
#     for j in range(1,10):
#         print(j) #72
        
# for i in range(2,10): # 2~9까지 8번 실행
#     print(i)
    
# for i in range(8): # 위와 다르게 0~7까지 실행
#     print(i)

# 5~21 까지 출력하시오.
# for i in range(5,22):
#     print(i)

# # 1,10 까지 출력하시오.
# for i in range(1,11):
#     print(i)

# # 0,9까지 출력하시오. 홀수만 출력하시오.
# for i in range(10):
#     if i%2 == 1:
#        print(i)
    
# for i in range(10):
#     if i%2 == 0:
#        continue
#     print(i,end=",")
    
    
# 구구단을 출력하시오.
# 방법 1
# print("[구 구 단]")
# for i in range(2,10):
#     if i%2==1:
#        print(" {}단".format(i))
#        for j in range(1,10):
#            print("{}x{}={}".format(i,j,(i*j)))
# print()

# 방법 2
# print("[구 구 단]")
# for i in range(2,10):
#     if i%2==0:continue
#     print(" {}단".format(i))
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,(i*j)))
# print()


# names = ['홍길동','유관순','이순신','김구','강감찬']
# # for 변수 in 범위: -> 범위안에 들어갈 수 있는 것들 : range,list,문자열,딕셔너리,튜플

# for name in names:
#     print(name) 

# for name in enumerate(names): # index번호, 값을 함께 리턴해줌 튜플 형태로 나옴 # (0, '홍길동') (1, '이순신') ...
#     print(name)

# for name in enumerate(names): #  0 홍길동 1 이순신 .....
#     print(name[0],name[1])

# for i,name in enumerate(names): #  0.홍길동 1.이순신 .....
#     print("{}.{}".format(i,name))

# n_list = [
#     [1,'홍길동'],
#     [2,'유관순'],
#     [3,'이순신']
# ]
# # 2차원 계열은 for문을 2번 사용
# for ns in n_list:  # n_list가 ns로 넘어가면서 반복
#     for n in ns:   # ns가 n로 넘어가면서 반복
#         print(n,end="")
#     print()
    
a_list = []
# for문을 사용해 0을 10개 들어가는 리스트를 만드세요.
# append 사용
# 방법1
for i in range(10):
    a_list.append('0')
print(a_list)
# 방법2  # 리스트 타입 변환
# 속도면에서 더 빠름
a_list = list('0'*10)
print(a_list)
# 방법3  # 리스트 내포 1,3번 방법 같은 형태임
# # 속도 면에서 제일 빠름, 숫자형태로도 가능
a_list = ['0' for j in range(10)]
print(a_list)
# 
a_list = [i*i for i in range(1,10)]
print(a_list)