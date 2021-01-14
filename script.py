
for x in range(6):
	from selenium import webdriver
	from selenium.webdriver import Chrome
	from selenium.webdriver.chrome.options import Options

	PATH = r"C:\Users\makon\Desktop\script\chromedriver.exe"
	driver = webdriver.Chrome(PATH)
	options = webdriver.ChromeOptions()

	driver.get('http://etc.ch/6rZq')
	driver.find_element_by_xpath("//span[@class='ui-btn-text']").click()
	driver.find_element_by_xpath("//input[@class='votebutton ui-btn-hidden']").click()
	driver.quit()

