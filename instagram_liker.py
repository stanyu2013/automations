from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(5)

driver.get('https://www.instagram.com/')
username = driver.find_element_by_name("username")
# enter your username
password = driver.find_element_by_name("password")
# enter your password

login  = driver.find_element_by_xpath("//div[text()='Log In']")
login.click()

sleep(5)

search = driver.find_element_by_xpath("//input[@placeholder='Search']")
search.send_keys('#coding')
sleep(2)

choices = driver.find_element_by_xpath("//a[@class='yCE8d  '][1]")
choices.click()

posts = driver.find_elements_by_class_name("v1Nh3")
for i in range(0,1000):	
	driver.find_elements_by_class_name('_9AhH0')[i].click()
	driver.find_elements_by_class_name('fr66n')[0].click()
	actions = ActionChains(driver)
	actions.send_keys(Keys.ESCAPE)
	actions.perform()
