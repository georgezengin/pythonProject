from time import sleep
from selenium import webdriver
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
# import KEYS
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('c:/DevExp/tip_calc/index.html')

billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")

driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
driver.find_element(by='id', value='peopleamt').send_keys('8')
driver.find_element(by='id', value='musicQual').send_keys('0',Keys.ARROW_DOWN)
#driver.find_element(by='id', value='musicQual').send_keys('0')
driver.find_element(by='id', value='calculate').click()
expected="2.38"

actual = driver.find_element(by="id", value='tip').text
assert  expected == actual, f"Expected: {expected}, Actual: {actual}"
#sleep(10)

# create action chain object
action = ActionChains(driver)
# get geeksforgeeks.org
action.key_down(Keys.CONTROL).send_keys('T').perform()
driver.get("https://www.geeksforgeeks.org/")

# perform the operation
action.key_down(Keys.CONTROL).send_keys('F').perform()

sleep(10)
