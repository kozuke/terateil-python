from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://www.python.org')

page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')
print('page_width', page_width, sep=':')
print('page_height', page_height, sep=':')
driver.set_window_size(page_width, page_height)

driver.save_screenshot('screenshot.png')
driver.close()
driver.quit()
exit()
