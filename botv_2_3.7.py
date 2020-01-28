from selenium import webdriver
import time
import os
import random
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

boolean = True


def threadfunc():
    global boolean
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    while boolean:
        time.sleep(random.randint(0, 3))
        driver.get("https://bannerweb.sabanciuniv.edu/")
        loginbutton = driver.find_element_by_css_selector("body > div > div.header > div:nth-child(2) > div > div > div > a")
        loginbutton.click()
        start = time.time()
        while driver.current_url != "https://suis.sabanciuniv.edu/prod/twbkwbis.P_SabanciLogin":

            end = time.time()
            limit = int(end - start)
            print(limit)
            if limit > random.randint(0, 4):
                break
        if driver.current_url == "https://suis.sabanciuniv.edu/prod/twbkwbis.P_SabanciLogin" and boolean:
            username = driver.find_element_by_name("sid")
            password = driver.find_element_by_name("PIN")
            username.send_keys("username")
            password.send_keys("password")
            time.sleep(random.randint(0, 3));
            submitbutton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.pagebodydiv > form > p > input[type=submit]")))
            submitbutton.click()
            time.sleep(random.randint(0, 3))
            studentbutton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                   " body > div.headerwrapperdiv > div.headerlinksdiv > span > map > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > a")))
            studentbutton.click()
            time.sleep(random.randint(0, 3))
            registerbutton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                    "body > div.pagebodydiv > table.menuplaintable > tbody > tr:nth-child(1) > td:nth-child(2) > a")))
            registerbutton.click()
            time.sleep(1)
            adddropbutton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                   "body > div.pagebodydiv > table.menuplaintable > tbody > tr:nth-child(2) > td:nth-child(2) > a")))
            adddropbutton.click()
            termbutton = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.pagebodydiv > form > input[type=submit]")))
            termbutton.click()
            input0 = driver.find_element_by_id("crn_id1")
            input1 = driver.find_element_by_id("crn_id2")
            input2 = driver.find_element_by_id("crn_id3")
            input3 = driver.find_element_by_id("crn_id4")
            input4 = driver.find_element_by_id("crn_id5")
            input5 = driver.find_element_by_id("crn_id6")
            input6 = driver.find_element_by_id("crn_id7")
            input7 = driver.find_element_by_id("crn_id8")
            input8 = driver.find_element_by_id("crn_id9")

            input0.send_keys("20306")
            input1.send_keys("20309")
            input2.send_keys("20485")
            input3.send_keys("20487")
            input4.send_keys("20488")
            input5.send_keys("20489")
            input6.send_keys("20498")
            input7.send_keys("20499")
            input8.send_keys("20494")


            finalbutton = driver.find_element_by_css_selector(
                "body > div.pagebodydiv > form > input[type=submit]:nth-child(23)")
            time.sleep(1)
            finalbutton.click()
            if not boolean:
                driver.close()
            if boolean:
                boolean = False
                driver.maximize_window()

            break


a = threading.Thread(target=threadfunc)
a.start()
time.sleep(random.randint(0, 4))
m = threading.Thread(target=threadfunc)
m.start()
time.sleep(random.randint(1, 4))
k = threading.Thread(target=threadfunc)
k.start()
time.sleep(random.randint(1, 4))
ga = threading.Thread(target=threadfunc)
ga.start()
time.sleep(random.randint(1, 4))
la = threading.Thread(target=threadfunc)
la.start()
time.sleep(random.randint(1, 4))
ta = threading.Thread(target=threadfunc)
ta.start()
time.sleep(random.randint(1, 4))
ma = threading.Thread(target=threadfunc)
ma.start()
time.sleep(random.randint(1, 4))
na = threading.Thread(target=threadfunc)
na.start()
time.sleep(random.randint(1, 4))
za = threading.Thread(target=threadfunc)
za.start()
time.sleep(random.randint(1, 4))
ooa = threading.Thread(target=threadfunc)
ooa.start()
time.sleep(random.randint(1, 4))
baa = threading.Thread(target=threadfunc)
baa.start()
time.sleep(random.randint(1, 4))
zaa = threading.Thread(target=threadfunc)
zaa.start()
#
print(random.randint(1, 100))
input('Press ENTER to exit')
