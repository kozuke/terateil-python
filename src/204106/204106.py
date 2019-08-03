import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.yahoo.co.jp")
time.sleep(5)

driver.close()
driver.quit()
