a_list = []
# 1. bbb파일 3개를 출력
f = open("C:/down/bbb.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "" : break
    a_list.append(txt.strip().split(",")) # 리스트 추가
    print(txt.strip())
    
        
        
# 3개를 a_list에 추가
# txt_list = f.readlines()
# for txt in txt_list:
#     print(txt.split())
    # a_list.append(txt.split())
    
print(a_list)
f.close






# 문자열 안에 \를 넣으면 문자로 인식
# print('안녕하세요. "홍길동"입니다')
# f = open("C:/down/aaa.txt","r",encoding="utf8")
# # while True:
# #     txt = f.readline()
# txt = "1,홍길동,100,100,100,300,100.00,0"
#     # if txt == "": break
#     # print(txt.strip())   # print(txt) 하면 엔터키(공백)가 적용되 출력되기 때문에 공백을 제거해주는거임
#     # # print(txt,end="")
# print(txt.strip())            # 문자열 타입 - strip(): 공백제거
# print(txt.strip().split(",")) # 쉼표 기준으로 리스트 형태로 나눠줌
# print(txt.strip().split(",")[5]) # 쉼표 기준으로 리스트 형태로 나눠고 인덱스 5번 출력
# # f.close()