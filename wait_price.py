from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    btn = driver.find_element_by_id('book')

    price = WebDriverWait(driver, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    btn.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    num = driver.find_element_by_id('input_value').text
    fin = calc(num)
    input = driver.find_element_by_id('answer').send_keys(fin)
    final_btn = driver.find_element_by_id('solve').click()

finally:
    time.sleep(5)
    driver.quit()
