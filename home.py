# Add comment

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")

SeleniumRuby = driver.find_element_by_css_selector("img[title='Selenium Ruby']")
SeleniumRuby.click()
Reviev = driver.find_element_by_css_selector(".reviews_tab a")
Reviev.click()

driver.execute_script("window.scrollBy(0, 800);")

Star_5 = driver.find_element_by_css_selector('a.star-5')
Star_5.click()
Comment = driver.find_element_by_id("comment")
Comment.send_keys("Nice book!")
Name = driver.find_element_by_id("author")
Name.send_keys("Ivan")
Email = driver.find_element_by_id("email")
Email.send_keys("ivan@email.com")
Submit = driver.find_element_by_css_selector("#submit.submit")
Submit.click()

driver.quit()
