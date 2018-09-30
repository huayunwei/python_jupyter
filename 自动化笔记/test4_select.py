from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('../webDriver/chromedriver.exe')

driver.get("https://www.baidu.com/")
driver.implicitly_wait(5)

setting = driver.find_element_by_link_text('设置')
time.sleep(2)
ActionChains(driver).move_to_element(setting).perform()
time.sleep(2)
searchSettion = driver.find_element_by_link_text('搜索设置')
searchSettion.click()
time.sleep(2)
select = driver.find_element_by_id('nr')
select.click()
time.sleep(2)
option = select.find_element_by_xpath("//option[@value='20']")
ActionChains(driver)