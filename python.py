from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

XPath = {
    'a' : '//*[@id="mail"]',
    'b' : '//*[@id="__next"]/div/main/div/div/div/div/div/form/div/div[1]/div[2]/input',
    'c' : '//*[@id="__next"]/div/main/div/div/div/div/div/form/div/div[2]/div/button',
    'd' : '//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a',
    'e' : '//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[3]/a',
    'f' : '//*[@id="__next"]/div/main/form/section/section[2]/div/div[1]/div[2]/input',
    'g' : '//*[@id="__next"]/div/main/form/section/section[2]/div/div[2]/div[2]/input',
    'h' : '//*[@id="__next"]/div/main/form/div/button'
}

def getMail(driver):
    driver.get('https://temp-mail.org/es/')

    time.sleep(10)

    return driver.find_element_by_xpath(XPath['a']).get_attribute('value')

def signUp(driver, mail):
    driver.get('https://www.geoguessr.com/signup')

    mailInput = driver.find_element_by_xpath(XPath['b'])
    mailInput.clear()
    mailInput.send_keys(mail)

    button = driver.find_element_by_xpath(XPath['c'])
    button.send_keys(Keys.ENTER)

    time.sleep(2)

def getVerification(driver):
    driver.get('https://temp-mail.org/es/')

    driver.minimize_window()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10, poll_frequency=2)
    message = wait.until(EC.presence_of_element_located((By.XPATH, XPath['d'])))
    message.click()

    return driver.find_element_by_xpath(XPath['e']).get_attribute('href')

def createAccount(driver, verificationUrl):
    driver.get(verificationUrl)

    passwordString = '12345678'

    password = driver.find_element_by_xpath(XPath['f'])
    password.send_keys(passwordString)

    pawssword2 = driver.find_element_by_xpath(XPath['g'])
    pawssword2.send_keys(passwordString)

    changeButton = driver.find_element_by_xpath(XPath['h'])
    changeButton.click()

    time.sleep(1)

def writeMail(mail):
    f = open("file.txt", "a")
    f.write(mail + '\n')
    f.close()

def main():
     driver = webdriver.Firefox(executable_path=r'./driver/firefox.exe')

     mail = getMail(driver)

     signUp(driver, mail)

     verificationUrl = getVerification(driver)

     createAccount(driver, verificationUrl)

     writeMail(mail)

     driver.close()

while 1:
    main()

    time.sleep(1)
