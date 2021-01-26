from selenium import webdriver
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


def mail_sender(mail_adresi):
    try:

        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login("email adresi", "email sifre")

        mesaj = MIMEMultipart()
        mesaj["From"] = "zehrckmk@gmail.com"
        mesaj["To"] = mail_adresi
        mesaj["Subject"] = "İş Başvurusu (Software Tester)"

        body = """

        Merhaba,

        2018 yılında Muğla Sıtkı Koçman Üniversitesi Metalurji ve Malzeme Mühendisliğinden mezun oldum.
        Ancak kendimi Software tester olarak geliştirmek istiyorum. Bunun için Selenium, Jira, WebAPI vb. Test Uzmanlığı ile ilgili
        eğitim aldım. Eğer şirketinizde software tester pozisyonunuz varsa sizinle 
        çalışmayı çok isterim. Benimle mail aracılığıyla ya da https://www.linkedin.com/in/zehra-%C3%A7-31a579144/ ile
        iletişime geçebilirsiniz. İstenildiği takdirde özgeçmişimi de yollayabilirim.

        Teşekkürler,
        İyi çalışmalar.

        Zehra ERTÜRK    


        Not: Mail adresiniz python ve selenium kullanılarak teknokent sitesi üzerinden alınmıştır ve bu mail otomatik olarak gönderilmiştir.
        """
        body_text = MIMEText(body, "plain")
        mesaj.attach(body_text)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

    except:
        print("hata: ", sys.exc_info()[0])


def main():
    browser = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver') #chromedriver dizini
    browser.get('http://odtuteknokent.com.tr/tr')
    time.sleep(2)

    for i in range(1, 418): #417 firmanın sayfasında dönerek mail adreslerini topla
        try:
            firmalar = browser.find_element_by_xpath('/html/body/div[2]/header/div[2]/div/div/div[2]/nav/ul/li[4]/a')
            firmalar.click()
            time.sleep(2)
            firma_ara = browser.find_element_by_xpath(
                '/html/body/div[2]/section[1]/div/div/div[2]/section/ul/li[' + str(i) + ']')
            firma_ara.click()
            browser.fullscreen_window()
            time.sleep(2)
            firmasayfasi = browser.find_element_by_xpath(
                '/html/body/div[2]/section[1]/div/div/div[1]/div[1]/div[2]/div/div/a')
            firmasayfasi.click()
            time.sleep(2)
            mail_adresi = browser.find_element_by_xpath(
                '/html/body/div[2]/section[1]/div/div[1]/div[2]/div[3]/div[1]/span/a')
            mail_sender(mail_adresi.text)
            time.sleep(2)
            print(mail_adresi.text, i, "adresine mail gönderilmiştir.")
        except Exception as e:
            print("Hata oluştu", e)

main()