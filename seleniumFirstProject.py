from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/Users/User/Desktop/chromedriver")

browser.get("https://www.linkedin.com/home")

browser.fullscreen_window()
time.sleep(2)

login = browser.find_element_by_css_selector("body > nav > div > a.nav__button-secondary")
time.sleep(2)
login.click()

time.sleep(2)

email = browser.find_element_by_xpath("//*[@id='username']")
password = browser.find_element_by_xpath("//*[@id='password']")

email.send_keys("email adresi")
password.send_keys("parola")

login_button = browser.find_element_by_css_selector("#app__container > main > div.card-layout > form > div.login__form_action_container > button")
login_button.click()
time.sleep(5)

arama_kutucugu = browser.find_element_by_xpath("//*[@id='ember20']/input")
arama_kutucugu.send_keys("#python")
arama_kutucugu.send_keys(Keys.RETURN)
time.sleep(6)

agim = browser.find_element_by_css_selector("#ember26")
agim.click()
time.sleep(5)

baglanti = browser.find_element_by_class_name("mn-community-summary__entity-info")
baglanti.click()
time.sleep(5)

for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
takipciler = browser.find_elements_by_class_name("mn-connection-card__details")
takipcilerList=[]

for takipci in takipciler:
    takipcilerList.append(takipci.text)

with open ("takipci.txt","w",encoding = "UTF-8") as file:
    for takipci in takipcilerList:
        file.write(takipci + "\n")

time.sleep(5)

browser.quit()