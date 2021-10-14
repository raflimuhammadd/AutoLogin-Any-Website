from selenium import webdriver

username = "input your website username or email"
password = "input your website password"

url = "input your website url"

driver = webdriver.Chrome("D://WebDriver//Chromedriver")

driver.get(url)

driver.find_element_by_id("input the id").send_keys(username)
driver.find_element_by_id("input th id").send_keys(password)
driver.find_element_by_id("input the id").click()

print("Log in Successfully")
