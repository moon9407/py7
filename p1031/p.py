import random

english = {
    '사랑':'love',
    '커피':'coffee',
    '컴퓨터':'computer',
    '이름':'name',
    '말하다':'say',
    '농장':'farm',
    '사과':'apple',
    '바나나':'banana',
    '책':'book',
    '강아지':'dog',
    '고양이':'cat',
    '컵':'cup',
    '박스':'box',
    '달걀':'egg',
    '생선':'fish',
    '엄마':'mother',
    '아빠':'father',
    '가족':'family',
    '버스':'bus',
    '날씨':'weather'
}

play = random.sample(list(english.items()),5)

print(play)