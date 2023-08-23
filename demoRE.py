# demoRE.py
import re

#search는 빈칸이 있더라도 같은 항목이 있으면 호출됨.
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())
#match는 정확히 일치하는 항목만 호출됨.
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

print("---연도를 찾는 경우---")
result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())
print("---우편번호를 찾는 경우---")
result = re.search("\d{5}", "우리 동네는 52300입니다.")
print(result.group())

