import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.casitabi.com/ja/")
time.sleep(10)
# username = driver.find_element_by_xpath('//*[@id="243c4fb9-7f4a-46d2-94ac-9676923d909e"]')
# //*[@id="243c4fb9-7f4a-46d2-94ac-9676923d909e"]

username = driver.find_element_by_css_selector(r'#\32 43c4fb9-7f4a-46d2-94ac-9676923d909e')
#\32 43c4fb9-7f4a-46d2-94ac-9676923d909e

print(username)
driver.close()
driver.quit()