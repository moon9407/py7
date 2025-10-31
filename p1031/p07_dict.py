import random

english = {
    '사랑':'love','커피':'coffee','컴퓨터':'computer','이름':'name',
    '말하다':'say','농장':'farm','사과':'apple','바나나':'banana',
    '책':'book','강아지':'dog','고양이':'cat','컵':'cup','박스':'box',
    '달걀':'egg','생선':'fish','엄마':'mother','아빠':'father',
    '가족':'family','버스':'bus','날씨':'weather'
}
# # 20문제 중 랜덤으로 5문제를 뽑아서 퀴즈를 만드세요.
a_list =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
quest = random.sample(a_list,5)
quest.sort()
quest_dic = {}      # 정답,오답 입력을 위한 공간
# print(quest)
count = 0
wrong = 0
num= 1

for i,k in enumerate(english.keys()): # index를 함께추출 , key
    if i in quest:
        # print(i,k,english[k])
        # 정답 입력
        print("{}은(는) 영어로 뭘까요?".format(k))
        answer = input(">>")
        # 정답확인
        if answer == english[k]:
            print("정답입니다!")
            print()
            count = count+1 # count += 1
            quest_dic[num] = "정답"
            
            
        else:
            print("오답! 정답은 {}입니다.".format(english[k]))
            print()
            wrong = wrong+1   
            quest_dic[num] = "오답"
        num = num+1

# # 1번:정답 2번 :오답
print(quest_dic)
print("정답개수 : {}개 오답개수 : {}".format(count,wrong))


# count = 0
# wrong = 0
# a_list = []
# play = random.sample(list(english.items()),5)

# for k,v in enumerate(play):


