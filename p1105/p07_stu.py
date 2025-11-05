# 학생성적 1명 클래스
class Student:
    
    def __init__(self,stuno,name,kor,eng,math):  # 객체 == 인스턴스
            # 키   =   값
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0

    # __str__: 객체, 참조변수를 출력하면 함수 실행을 시킴
    def __str__(self):
        return (f"{self.stuno}\t{self.name}\t{self.kor}\t")
        

    def s_total(self):
        self.total = self.kor+self.eng+self.math
    def s_avf(self):
        self.avg = self.total/3

# 학생성적리스트 클래스
class Students:
    stu_list = []
    def add(self,student):
        self.stu_list.append(student)

            
stus = Students()
            
stus.add(Student(10101,'홍길동',100,100,100))
stus.add(Student(10102,'유관순',90,100,100))
stus.add(Student(10103,'이순신',80,100,100))

print(Student(10101,'홍길동',100,100,100))

