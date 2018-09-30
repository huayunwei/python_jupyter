from selenium import webdriver
import time

driver = webdriver.Chrome('../webDriver/chromedriver.exe')

# 跳转
driver.get('http://qz.6kena.com/manage/login')
time.sleep(2)

# 跳转
driver.get('http://www.baidu.com')
time.sleep(2)

# 返回
driver.back()
time.sleep(2)

# 前进
driver.forward()
time.sleep(2)

# 刷新
driver.refresh()
time.sleep(2)

# 获取标题
print(driver.title)
# 获取当前url
print(driver.current_url)
# 获取整个页面 --- 可以用于beautifulsoup
print(driver.page_source)


# 当前窗口的大小:数据格式--{'width': 1050, 'height': 708}
print(driver.get_window_size(windowHandle='current'))
time.sleep(2)

# 最大化窗口
driver.maximize_window()
time.sleep(2)

# 设置窗口的大小
driver.set_window_size(1000,1000)
time.sleep(2)

driver.get('http://www.silianchina.com/')

# 截屏
# 需要以png结尾：It should end with a `.png` extension，不过不影响保存为.jpg格式的文件
driver.get_screenshot_as_file('C:\\Users\\MissFe\\Desktop\\pic.png')
time.sleep(2)

# 截屏返回图片的base64编码
print(driver.get_screenshot_as_base64())
time.sleep(2)

# 截屏返回图片的二进制编码
print(driver.get_screenshot_as_png())
time.sleep(2)


# 退出
driver.close() # 关闭当前窗口
driver.quit() # 退出浏览器进程