# return: 함수호출로 값을 전달할 때 사용

def cal(a,b):
    return a+b # 함수 호출로 값을 전달
sum = cal(1,2)

def func(a,b):
    a+b
    return     # 리턴에 값이 없으면 함수 종료, 리턴 자리에 있는것만 전달해줌

def big(a,b):
    c = 0
    if a>b:
        return a
    else:
        return -1  #무언가는 돌려주는게 좋음

