from selenium import webdriver
import time
browser = webdriver.Chrome("C:\\Users\\User\\Desktop\\chromedriver")

browser.get("https://www.instagram.com/")
time.sleep(2)
email = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

email.send_keys('email')
password.send_keys('şifre')

login_button = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login_button.click()
time.sleep(5)

not_now = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
not_now.click()
time.sleep(8)

browser.quit()