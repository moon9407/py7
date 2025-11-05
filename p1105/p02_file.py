import os

# 파일 복사 - 문자읽기:r, 문자쓰기:w /파일읽기:rb 파일쓰기 : wb
f = open("c:/down/dog1.jpg","rb")
f2 = open("c:/aaa/dog1.jpg","wb")

while True:
    dfile = f.read(1)   # read(): 파일읽기, # readline(),readlines() : 문자읽기 
    if not dfile: break
    f2.write(dfile)

f.close()
f2.close()
print("복사완료")

# with open() 파일 입출력
# with open ("c:/down/bbb.txt","r",encoding="utf-8") as f:
#     while True:
#         txt = f.readline()
#         if txt == "": break
#         print(txt.strip())
# # f.close 자동으로 입력됨

# f = open("c:/down/bbb.txt","r",encoding="utf-8")
# while True:
#     txt = f.readline()
#     if txt == "": break
#     print(txt.strip())
# f.close()



# 추가모드------------------------------------------------
# a : 추가모드
# f = open("C:/down/ccc.txt","a") # 있는 파일에 수정
# for i in range(5):
#     f.write(f"안녕하세요.{i}\n")

# f.close
# print("완료")

# 파일 쓰기------------------------------------------------
# w : 쓰기모드
# f = open("C:/down/ccc.txt","w") # 파일이 없으면 w모드는 파일을 생성 (새로할 때 마다 덮어쓰기)
# stu_data = ""
# for i in range(1):
#     txt = input("글자를 입력하세요. >> \n")
#     stu_data += txt+"\n"
# f.write(stu_data)
# f.close()
# print("완료")

# 파일 읽기모드------------------------------------------------
# r : 읽기모드
# 1. 통로(stream) : 파일 열기
# f = open("C:\workspaece\py7\p1105/studata.txt","r")    
# f = open("C:/down/aaa.txt","r",encoding="utf8")           # 한글일땐 encoding="utf8 추가 #euc-kr(국내표준), utf-8(국제표준), utf8
# while True:
#     txt = f.read()
#     if txt == "": break
#     print(txt,end="")


# read():1글자씩 읽어와서 넘겨줌(속도느림)
# readline(): 1줄씩 가져옴
# while True:
#     txt = f.readline()
#     if txt == "":break
#     print(txt,end="") # print 완료 후 줄바꿈 해줌.  end=""

# readlines() 전체 한번에 읽어옴(데이터가 크면 오류가능성)
# txt_list = f.readlines()         # 1줄씩 리스트에담아서 가져옴.
# print(txt_list)                  #['안녕하세요.\n', '반갑습니다.\n', '다음에 봐요\n', 'hello\n', 'see you']

# for txt in txt_list:
#     print(txt,end="")



# 2.통로 닫기
# f.close()   



#파일 추가모드------------------------------------------------