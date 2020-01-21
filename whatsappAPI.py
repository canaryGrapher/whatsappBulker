import webbrowser
import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

countryCode = input("Country code for this batch: ")
with open("rawNumber.txt", "r") as g:
    numberPerson = g.readline()
    with open("file.txt", "w") as q:
        for line in g:
            numberOfPerson = line[:-1]
            header = "https://api.whatsapp.com/send?phone="
            number = "+" + str(countryCode) + numberOfPerson
            addMessage = "&text="
            message = "Hello automation"
            q.write(header)
            q.write(number)
            q.write(addMessage)
            q.write(message)
            q.write("\n")
    q.close()
g.close()
driver = webdriver.Firefox()
x = 0
with open("file.txt", "r") as f:
    for line in f:
        print(line)
        driver.get(line)
        # webbrowser.open(line)
        time.sleep(5)
        elementFirst = driver.find_element_by_xpath("//*[@id='action-button']")
        elementFirst.click()
        driver.implicitly_wait(4)
        elementSecond = driver.find_element_by_link_text("use WhatsApp Web").click()
        # textbox.sendKeys(Keys.RETURN);
        if x==0:
            print("Waiting for user to sign in")
            time.sleep(15)
            x = x + 1
            elementThird = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()
            body = driver.find_element_by_tag_name("body")
            driver.implicitly_wait(4)
            body.send_keys(Keys.CONTROL + 'w')
        driver.implicitly_wait(4)
        time.sleep(10)
        elementThird = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()
        body = driver.find_element_by_tag_name("body")
        driver.implicitly_wait(4)
        body.send_keys(Keys.CONTROL + 'w')
driver.close()
