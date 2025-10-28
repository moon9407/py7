# 조건문 : if문,    swith문은 파이썬에 없음
# 반복문 - 여러번 실행
# for(), while()

# 문자열 슬라이싱[시작:끝-1:스텝]
# range:범위 ,range(10) 10번 반복
# range(시작,끝,스텝), range(끝) :0 ~ 끝-1
# for 변수 in 범위 - 문법
for i in range(10): # 0 ~ 9
    print(i)
    
    
for i in range(5): # 0 ~ 4 5번실행
    print("안녕하세요.")

for _ in range(5): # 0 ~ 4 5번실행
    print("hello.")
    
for i in range(5): # 0 ~ 4 5번실행
    print(i+1,"번째 안녕")
    
for i in range(1,6): # 1 ~ 5번까지 5번실행
    print(i,"번째")

for i in range(1,11,2): # 1 ~ 10번까지 10번실행 2번씩 건너뛰며
    print(i,"번째")
    
sum = 0
for i in range(1,11):
    sum = sum + i
   # print(i,"번째:",sum)
    print("{}번째: {}".format(i,sum))
    
print("총합계 :",sum)


a_list = ["홍길동",100,90,80] # 리스트 하나씩 뽑아옴
for a in a_list : # a_list[0],a_list[1],a_list[2],a_list[3]
    print(a)
    
# 2차원리ㅡ트 - for문 2번, 3차원리스트 - for문 번

name = "홍길동유관순이순신"
for i in name:
    print(i)


# range() 숫자를 입력하세요. 10번 출력
sum = 0
for i in range(10):
    num = int(input("{}번째 숫자를 입력하세요.".format(i+1)))
    sum = sum + num
    
print("합계 :",sum)
    #print(i+1,"번째 숫자를 입력하세요.")
    #print("{}번째 숫자를 입력하세요.".format(i+1))

# num = input("숫자를 입력하세요.")
# for i in range(10):
#    print(num)


