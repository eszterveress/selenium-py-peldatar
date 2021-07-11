from selenium import webdriver

PATH = "D:\programok\selenium\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("https://www.w3schools.com/python/default.asp")
browser.close()
