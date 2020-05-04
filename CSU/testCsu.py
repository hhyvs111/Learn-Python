# -*- coding: utf-8 -*
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  # 提供键盘按键支持（最后一个K要大写）

driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.python.org")  # 这个时候chromedriver会打开一个Chrome浏览器窗口，显示的是网址所对应的页面
