# class01.py
#1) 클래스 형식을 정의
class Person: 
    #초기화 메소드
    def __init__(self):
        #인스턴스 멤버 변수 초기화
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()

#3)메서드 호출
p1.name = "이다빈"
p1.print()
p2.print()

#런타임(코드가 실행되는 시점) --> 자동완성 되지 않는 기능은 사용하지 않는 것이 좋음
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

#인스턴스에 추가 --> 인스턴스에 추가하더라고 error 발생. 사용하지 않는 것이 좋음.
p1.age = 30
print(p1.age)
# print(p2.age)
# print(Person.age)

