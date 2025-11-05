# 문자열 안에 \를 넣으면 문자로 인식
# print('안녕하세요. "홍길동"입니다')
f = open("C:/down/aaa.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "": break
    print(txt,end="")

f.close()