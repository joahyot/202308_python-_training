# ChatGPT클래스생성.py
# 'Person' 클래스를 정의합니다. 'id'와 'name' 멤버 변수를 가지며 'printInfo()' 메서드가 있습니다.
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}")
        print(f"이름: {self.name}")


# 'Manager' 클래스를 정의합니다. 'Person' 클래스를 상속하며 'skill' 멤버 변수를 추가합니다.
class Manager(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)  # 부모 클래스의 생성자를 호출합니다.
        self.skill = skill

    def printInfo(self):
        super().printInfo()  # 부모 클래스의 'printInfo()' 메서드를 호출합니다.
        print(f"기술: {self.skill}")


# 'Employee' 클래스를 정의합니다. 'Person' 클래스를 상속하며 'role' 멤버 변수를 추가합니다.
class Employee(Person):
    def __init__(self, id, name, role):
        super().__init__(id, name)  # 부모 클래스의 생성자를 호출합니다.
        self.role = role

    def printInfo(self):
        super().printInfo()  # 부모 클래스의 'printInfo()' 메서드를 호출합니다.
        print(f"역할: {self.role}")


# 예시 테스트 케이스
manager1 = Manager(101, "Eve", "문제 해결")
manager1.printInfo()

employee1 = Employee(201, "Charlie", "디자이너")
employee1.printInfo()

manager2 = Manager(102, "Grace", "커뮤니케이션")
manager2.printInfo()

employee2 = Employee(202, "David", "테스터")
employee2.printInfo()

manager3 = Manager(103, "Frank", "기술 전문성")
manager3.printInfo()

employee3 = Employee(203, "Emma", "분석가")
employee3.printInfo()

manager4 = Manager(104, "Henry", "팀 관리")
manager4.printInfo()

employee4 = Employee(204, "Olivia", "작가")
employee4.printInfo()

manager5 = Manager(105, "Isaac", "혁신")
manager5.printInfo()

employee5 = Employee(205, "Liam", "지원")
employee5.printInfo()
