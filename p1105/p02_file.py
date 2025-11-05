import os

# 1. 통로(stream) : 파일 열기
# r(read):읽기모드 w(write):쓰기모드 a(append):추가하기 
# f = open("C:\workspaece\py7\p1105/studata.txt","r")    
f = open("C:/down/aaa.txt","r",encoding="utf8")           # 한글일땐 encoding="utf8 추가 #euc-kr(국내표준), utf-8(국제표준), utf8
while True:
    txt = f.read()
    if txt == "": break
    print(txt,end="")


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
f.close()   