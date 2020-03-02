from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

driver = webdriver.Chrome()
now = datetime.datetime.now()
# go to site
driver.get("https://google.com")
# read file
f = open('in.txt', 'r')
# search query
elem = driver.find_element_by_name("q")
fr = f.read()
elem.send_keys(fr)
elem.send_keys(Keys.RETURN)
# compare file with caption page
if fr == driver.title.replace(' - Поиск в Google', ''):
    f = open("out.txt", "a")
    f.write("мы на нужной странице")
else:
    f = open("error.txt", "a")
    f.write("ошибка")
    f.close()
    driver.save_screenshot('.\\\\screen\\' + now.strftime("%d-%m-%Y_%H-%M") + '.png')
