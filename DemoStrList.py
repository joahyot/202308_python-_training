# DemoStrList.py
# 실행: ctrl + F5
strA = "python is very powerful"
strB = "파이썬은 강력해"
strC = """파이썬을
오늘부터
학습합니다."""

print(strA)
print(len(strB))
print(len(strC))
print(strC)

result = "py" + "thon"
print(result)

#Slicing(indexing)
print(strA[0])
print(strA[0:6])
#약식(축약)
print(strA[:6])
print(strA[-3:])

print("---list 형식---")
lst = [1,2,3,4,5]
print(len(lst))
print(lst[0])
lst.append(10) # 추가 method
lst.insert(1,20)
print(lst)

colors = ["red", "blue", "green"]
colors +=["red"] # 사용하지 않는 것이 좋음
colors += "red" # 사용하지 않는 것이 좋음 
print(colors)
colors.remove("red") # 삭제 method
print(colors)
# 디버깅 할 때 중담점 (Break point)
for item in colors:
    print(item)

print("---tuple---")
tp = (10, 20, 30)
print(len(tp))
print(tp)
print("id:%s, name:%s" % ("Lee", "Dabin"))

#함수 정의 
def times(a,b):
    return a+b, a*b

#함수 호출
print(times(5,6))

args = (3,4)
print(times(*args))

print("---형식변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)

print("---set---")
a = {1,2,3,3}
b = {3,4,4,5}
print(len(a))
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
# print(a[0]) --> Error. set에서는 slicing 불가
