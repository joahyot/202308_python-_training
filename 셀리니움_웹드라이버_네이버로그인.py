# 셀리니움_웹드라이버_네이버로그인.py
# pip install clipboard 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login')

# 네이버 메인화면에서 로그인 버튼 클릭
# driver.find_element_by_xpath('//*[@id="account"]/a').click()
# time.sleep(1)   # 1초 시간 지연

# 로그인 창에 아이디/비밀번호 입력
loginID = "rhfld25"
clipboard.copy(loginID)
#mac은 COMMAND, window는 CONTROL
#XPATH; 계층구조로 접근할 수 있도록 함
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v')

loginPW = "rhfldrhfld25%"
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()


loginPN = "01057821258"
clipboard.copy(loginPN)
driver.find_element(By.XPATH,'//*[@id="phone_value"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="oab.submit"]').click()
# <input type="tel" name="" id="phone_value" placeholder="휴대전화 번호" class="int">
# <input type="submit" title="확인" alt="확인" value="확인" class="btn int_ok" id="oab.submit">


while True:
    pass 
