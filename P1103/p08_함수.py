
# 매개변수 개수는 호출하는 변수의 개수와 동일
# 매개변수 타입도 호출하는 변수타입과 동일해야함
# def add(a,b):
#     return a+b

# a = add(1,2)
# print(a)

# 가변 매개변수
# def add(a,b,*c): #변수앞에 *를 붙이면 가변 매개변수가 됨., 가변 매개변수에 들어오는것들은 리스트처리됨.
#     sum = a+b
#     for i in c:  # c : 여러개 가능.
#         sum += i
#     return sum

# print(add(1,2,3,4,5,6))


# def print_str(a,b,*c):
#     for i in c:
#         print(i)

# print_str("안녕","사과","홍길동","점수",100)

# 여러개를 입력받아, 함수를 사용해 출력하시오,
# def print_str(*c):
#     for i in c:
#         print(i)
        
# # 5번 입력받아 모두 출력하시오.
# str1 = [0,0,0,0,0]
# for i in range(5):
#     str[i] = input("아무 글자나 입력하세요.")

# print_str(*srt1)

stus = [1,'홍길동',100,90,80]

# 국어 영어 수학 점수를 입력받아 return 을 적용
def sum(kor,eng,math):
    return kor+eng+math


def avg(kor,eng,math):
    return (kor+eng+math)/3

# stus = [1,'홍길동',100,90,80]
# 함수를 제대로 구성해서 stus 리스트를 아래와 같이 변경하시오.
#stus = [1,'홍길동',100,90,80,270,90,00]으로 변경

sum = sum(stus[2],stus[3],stus[4])
stus.append(sum)
print(stus)

stus.append(avg(stus[2],stus[3],stus[4]))
print(stus)