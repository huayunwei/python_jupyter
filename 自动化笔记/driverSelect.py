'''
根据需要选择不同的driver


'''

from selenium import  webdriver
def driver():
    driver = webdriver.Chrome('../webDriver/chromedriver.exe')

    return driver