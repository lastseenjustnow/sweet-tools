from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib

from python_rucaptcha import ImageCaptcha

from datetime import timedelta, date, datetime

import time
import sys
sys.path.append(".")


from aux.auxiliary_functions import daterange_delta89
from rucaptcha_key import RUCAPTCHA_KEY
# create dates range


start_date = date(2019, 1, 1)
end_date = date(2020, 1, 1)
dates = []
for single_date in daterange_delta89(start_date, end_date):
    dates.append(single_date.strftime("%d/%m/%Y"))

driver = webdriver.Safari()
driver.get('http://domains.ihead.ru/domains/csv.html')

domains = ["ru", "su", "rf"]

for domain in domains:
    for date_begin in dates:

        driver.get('http://domains.ihead.ru/domains/csv.html')
        driver.set_window_size(1024, 768)

        element = driver.find_element_by_xpath(
            "/html/body/table[4]/tbody/tr[1]/td[2]/form/table/tbody/tr[1]/td[2]/select")
        element = Select(element)
        element.select_by_value("new")

        element = driver.find_element_by_xpath(
            "/html/body/table[4]/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td[2]/select")
        element = Select(element)
        element.select_by_value(domain)

        element = driver.find_element_by_name("date1")
        element.send_keys(date_begin)

        temp = datetime.strptime(date_begin, '%d/%m/%Y') + timedelta(88)
        date_end = temp.strftime("%d/%m/%Y")

        element = driver.find_element_by_name("date2")
        element.send_keys(date_end)

        # Catch captcha
        element = driver.find_element_by_xpath(
            "//td[@class='cb']/form[1]/table[1]/tbody[1]/tr[6]/td[2]/img")
        src = element.get_attribute('src')
        urllib.request.urlretrieve(src, "screenshot.png")

        # Solve captcha
        image_link = "screenshot.png"
        user_answer = ImageCaptcha.ImageCaptcha(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(captcha_file=image_link)

        if user_answer['errorId'] == 0:
            # решение капчи
            print(user_answer['captchaSolve'])
            print(user_answer['taskId'])
        elif user_answer['errorId'] == 1:
            # Тело ошибки, если есть
            print(user_answer['errorBody'])

        element = driver.find_element_by_name("keystring")
        element.send_keys(user_answer['captchaSolve'])

        element = driver.find_element_by_xpath(
            "//table[@class='body']/tbody[1]/tr[1]/td[2]/form[1]/table[1]/tbody[1]/tr[7]/td[1]/input[1]")
        element.send_keys(Keys.RETURN)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='body']/tbody[1]/tr[1]/td[2]/p[4]/a")))
        element.click()

        time.sleep(1)
