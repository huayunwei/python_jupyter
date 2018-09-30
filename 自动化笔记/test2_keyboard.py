from selenium import webdriver
import time
# Keys文件定义了键盘按键
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('../webDriver/chromedriver.exe')

# 打开本地html文件，注意一定要写url地址，直接写文件无法打开
driver.get('https://www.baidu.com/')
driver.implicitly_wait(4)

input = driver.find_element_by_id('kw')

input.send_keys('你好')
time.sleep(2)

# 执行搜索
input.submit()
time.sleep(2)

# 清空输入框
input.clear()
time.sleep(2)

# 重新输入
input.send_keys('再次输入')
time.sleep(2)
# 模拟键盘回车
# 数字键盘：NUMPAD2 -- 2
input.send_keys(Keys.NUMPAD2)
time.sleep(2)
# 键盘中的回车键
input.send_keys(Keys.ENTER)
time.sleep(2)
# 复制和粘贴
# 全选
input.send_keys(Keys.CONTROL,'a')
time.sleep(2)
# 复制
input.send_keys(Keys.CONTROL,'c')
time.sleep(2)
# 取消全选状态
input.send_keys(Keys.END)
time.sleep(2)
# 粘贴
input.send_keys(Keys.CONTROL,'v')