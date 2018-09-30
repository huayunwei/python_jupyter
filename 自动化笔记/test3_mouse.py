from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('../webDriver/chromedriver.exe')

driver.get('https://www.baidu.com/')
driver.implicitly_wait(4)

setting = driver.find_element_by_link_text('设置')
news = driver.find_element_by_link_text('新闻')
'''
 鼠标动作需要统一用perform函数执行，
 可以放在每个动作后，
 在所有动作之后单独放置，动作会按照顺序依次执行

# 写法1：放在每个动作后
ActionChains(driver).move_to_element(setting).perform()
'''

#写法2：在所有动作后单独放置
action = ActionChains(driver)
action.move_to_element(setting)
action.pause(2)
# 移动到另外一个元素
action.move_to_element(news)
action.pause(2)
# 点击
action.click()
action.perform()
time.sleep(2)

# 回退
driver.back()
time.sleep(2)
'''
此时和之前的页面不是一个页面了，即driver已经改变了
如果不获取直接使用之前页面的获取到的元素会报错：
selenium.common.exceptions.StaleElementReferenceException: 
Message: Element not found in the cache - perhaps the page has changed since it was looked up
'''
news = driver.find_element_by_link_text('新闻')
map = driver.find_element_by_link_text('地图')
# 此时action也必须重新定义
action = ActionChains(driver)
# 移动到new元素上
action.move_to_element(news)
action.pause(2)
# 点击map元素，如果不增加on_element直接click，会点击当前鼠标所在位置，如果增加该属性点击为该属性对应的元素
action.click(on_element=map)
action.pause(2)
#action.reset_actions()  # 清空动作列表
action.perform() # 整体执行


