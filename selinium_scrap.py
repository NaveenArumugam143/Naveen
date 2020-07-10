from selenium import webdriver

driver=webdriver.Chrome("chromedriver.exe")

driver.get("https://www.mohfw.gov.in/")

print(driver.find_element_by_tag_name("li> strong"))

