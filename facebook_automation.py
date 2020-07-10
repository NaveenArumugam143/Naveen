from  selenium import webdriver


driver=webdriver.Chrome("chromedriver.exe")
driver.get("https://www.facebook.com")
driver.find_element_by_name("email").send_keys("8523989616")

driver.find_element_by_name("pass").send_keys("naveenarumugam")
driver.find_element_by_id("u_0_b").click()


