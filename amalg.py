from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass


print("SBI")
x = raw_input("Username\n")
xx= getpass.getpass()
print("\nICICI")
y = raw_input("Username\n")
yy = getpass.getpass()

driver1=webdriver.PhantomJS()
driver1.implicitly_wait(4)
driver1.get("https://www.onlinesbi.com/")


driver2=webdriver.PhantomJS()
driver2.implicitly_wait(5)
driver2.get("https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI")

cid2 = driver2.find_element_by_xpath(".//*[@id='AuthenticationFG.USER_PRINCIPAL']")
cid2.send_keys(y)

login1 = driver1.find_element_by_xpath(".//*[@id='banking']/div[1]/div/a[1]")
login1.click()
cont_login1 = driver1.find_element_by_xpath(".//*[@id='phishing_banner']/div/a")
cont_login1.click()

username1 = driver1.find_element_by_xpath(".//*[@id='username']")

username1.send_keys(x)

password1 = driver1.find_element_by_xpath(".//*[@id='label2']")
password1.send_keys(xx)

submit1 = driver1.find_element_by_xpath(".//*[@id='Button2']")
submit1.click()

close1 = driver1.find_element_by_xpath(".//*[@id='p_cls_rec']/a/img")
close1.click()

password2 = driver2.find_element_by_xpath(".//*[@id='AuthenticationFG.ACCESS_CODE']")
password2.send_keys(yy)

login2 = driver2.find_element_by_xpath(".//*[@id='VALIDATE_CREDENTIALS1']")
login2.click()

f=driver2.page_source.find("INR ")

clickforb1 = driver1.find_element_by_xpath(".//*[@id='dr1']/td[3]/a")
#print(clickforb.text)
clickforb1.click()

time.sleep(1)

account1 = driver1.find_element_by_xpath(".//*[@id='dr1']/td[1]").text


balance2 = ''
for character in driver2.page_source[f:f+100]:
 if character=='<':
  break
 balance2 = balance2 + character
 
logout2 = driver2.find_element_by_xpath(".//*[@id='HREF_Logout']")
logout2.click()

balance1 = driver1.find_element_by_xpath(".//*[@id='accBalRes"+account1+"']").text
logout1= driver1.find_element_by_xpath(".//*[@id='tblContainer']/tbody/tr/td/table[2]/tbody/tr/td[9]/span/a")
logout1.click()
driver1.quit()
print("SBI")
print(balance1)
print("ICICI")
print(balance2)
