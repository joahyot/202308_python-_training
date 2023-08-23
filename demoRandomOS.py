# demoRandomOS.py

import random

print(random.random())
print(random.random())
print(random.uniform(2,6))
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("---샘플링---")
#sample; 유일한 숫자만 호출되도록 함
print(random.sample(range(20), 6))
print(random.sample(range(20), 6))

from os.path import *
from os import *

print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))

if exists("c:\\python310\\python.exe"):
    print("파일크기: {0}".format(getsize("c:\\python310\\python.exe")))
else:
    print("파일 없음")

print("운영체제이름:{0}".format(name))
print("환경변수:{0}".format(environ))
# system("notepad.exe")

#파일 목록
import glob
result = glob.glob("c:\\work\\*.py")
for item in result:
    print(item)



