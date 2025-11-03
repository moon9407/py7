# 문자열 함수

###### .upper() - 대문자로 변경 
###### .lower() - 소문자로 변경 
# .swapcase() - 대->소, 소->대로 변경
# .title() - 첫글자를 대문자로 변경

# a = 'abc'
# print(a.upper())
# b = 'aBBcFf'
# print(b.upper())


# 문자열 찾기
###### .count() - 해당되는 문자 갯수를 출력
###### .find() - 해당문자 위치 검색 없을 떄 -1 리턴
# .index() - 해당문자 위치 검색 - 없을 때 에러
###### .startswith() - 해당 문자로 시작 되는지 확인 , True와False로 출력
###### .endswith() - 해당 문자로 끝나는지 확인, True와False로 출력

# 공백제거
a= "    a b c   "
###### strip() - 좌우 공백 제거, 문자사이 공백은 제거되지 않음.
# print(a.strip())
# rstrip() - 오른쪽 공백제거
# print(a.rstrip())
# lstrip() - 왼쪽 공백제거
# print(a.lstrip())
# replace(변경 전 문자, 변경 후 문자) - 문자열 변경
# print(a.replace(' ','')) 
# split() - 문자열 분리 : 타입은 리스트로 분리해줌

# join() : 문자열 결합
# ss = "-"
# print(ss.join('파이썬')) # 파-이-썬

# map() : 리스트를 입력받아 처리하는 함수
# map(functhion함수부분, 리스트데이터)
# def multi(x):
#     return x*2
# a = [1,2,3]
# b = list(map(multi,a))
# print(a)
# print(b)

# a = ['100','90','80']
# print(map(int,a))  #리스트로 변환해줘야함
# b = list(map(int,a))   # map타입객체로 저장
# print(a)
# print(b)

# a = ['100','90','80']
# b = []
# for i in a:
#     b.append(int(i))
    
# print(a)
# print(b)

### isdigit() : 숫자인지 확인
### isalpha(): 문자(영문자,한글)확인
### isalnum(): 문자(영문자,한글), 숫자인지 확인
# islower(): 소문자 확인
# isupper(): 대문자 확인

# 국어점수를 입력하세요.
while True:
    kor = input("국어점수를 입력하세요.")
    if kor.isdigit(): # 숫자인지 확인
        break
    else:
        print("숫자가 아닙니다. 다시 입력하세요.")
print("숫자로 변경:",int(kor))




# a = '1,홍길동,100,100,100,300,100.0'
# titles = ['번호','이름','국어','영어','수학','합계','평균']

# print(sep: 변수 사이사이 모두 적용,end : 마지막에 한번 적용)
# print(*titles,sep='/',end='**') # 키워드 매개변수

# # print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles)) # 위와 같음
# a_list = a.split(",")
# print(*titles,sep='\t') # ,sep=''  사이 간격 출력
# print("-"*50)
# print(*a_list,sep='\t')


# a_list = a.split(',')
# print(a_list) # a_list[] : 원하는 인덱스 값만 나옴 int앞에 붙이면 숫자타입으로 변경
# b = '홍길동 유관순 이순신 김구'
# b_list = b.split(' ')
# print(b_list)
# print(b_list[1])





# a = "홍길동은 키가 180, 홍길동은 몸무게 70, 홍길동은 사는 곳은 서울입니다."
# print(a.replace('홍길동','홍길자'))


# input1 = input("이름을 입력하세요.>>   ").replace(' ','')   # :    홍길동 은 가능, 홍 길동 은 불가
# if '홍길동' == input1:
#     print("맞습니다.",input1)
# else:
#     print("틀립니다.",input1)
    


# print(a.count('3')) # 3은 5개 존재를 출력
# a = '112233333445'
# b = '프로그램 중 파이썬 사용자가 제일 많습니다.(파이썬 프로그래밍)'
# print(b.find('파이썬')) # 파이썬 위치 검색
# print(b.rfind('파이썬')) # 오른쪽 부터 위치 검색
# print(b.index('파이썬')) # 파이썬 위치검색, 없을 때 에러
# print(b.startswith('파이썬')) # 파이썬 위치검색, 없을 때 에러

# c= "abc.exe"
# print(c.endswith("xls"))




# # 문자열
# # 문자열 슬라이싱
# a = '안녕하세요'
# # 하세를 출력하세요
# print(a[2:4])
# print('안녕'*3)
# print('안녕'+'hello') # 연결연산자


