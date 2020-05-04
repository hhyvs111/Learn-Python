from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")

driver.maximize_window()

url = 'https://wxxy.csu.edu.cn/ncov/wap/default/index?from=history'
username = '176712082'
password = '19960302'

driver.get(url)
driver.find_element("name","username").send_keys(username)

driver.find_element("name","password").send_keys(password)

driver.find_element("name","Submit").click()
