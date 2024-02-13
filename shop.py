# 1 Страница товара

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

My_Account = driver.find_element_by_id("menu-item-50")
My_Account.click()

Username = driver.find_element_by_id("username")
Username.send_keys("ivanov@email.com")
Password = driver.find_element_by_id("password")
Password.send_keys("7_FJucizqG")
Login = driver.find_element_by_name('login')
Login.click()

Shop = driver.find_element_by_id("menu-item-40")
Shop.click()

driver.execute_script("window.scrollBy(0, 500);")

HTML5_Forms = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']")
HTML5_Forms.click()

H1 = driver.find_element_by_css_selector("div h1")
H1_text = H1.text
assert H1_text == "HTML5 Forms"

driver.quit()

# 2 Колличество товаров в категории

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

My_Account = driver.find_element_by_id("menu-item-50")
My_Account.click()

Username = driver.find_element_by_id("username")
Username.send_keys("ivanov@email.com")
Password = driver.find_element_by_id("password")
Password.send_keys("7_FJucizqG")
Login = driver.find_element_by_name('login')
Login.click()

Shop = driver.find_element_by_id("menu-item-40")
Shop.click()

HTML = driver.find_element_by_css_selector(".cat-item-19 a")
HTML.click()

Products = driver.find_elements_by_css_selector('.masonry-done li')
Products_len = len(Products)
assert Products_len == 3

driver.quit()

# 3 Сортировка товаров

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

My_Account = driver.find_element_by_id("menu-item-50")
My_Account.click()

Username = driver.find_element_by_id("username")
Username.send_keys("ivanov@email.com")
Password = driver.find_element_by_id("password")
Password.send_keys("7_FJucizqG")
Login = driver.find_element_by_name('login')
Login.click()

Shop = driver.find_element_by_id("menu-item-40")
Shop.click()

Default = driver.find_element_by_css_selector("[value='menu_order']")
Value_Default = Default.get_attribute("selected")
if Value_Default is not None:
    print("Выбрано значение по умолчанию")
else:
    print("Выбрано другое значение")

selector = driver.find_element_by_class_name("orderby")
Sorting = Select(selector)
Sorting.select_by_value("price-desc")

Sort_by_price = driver.find_element_by_css_selector("select [value='price-desc']")
Sort_by_price_selected = Sort_by_price.get_attribute("selected")
if Sort_by_price_selected is not None:
    print("Выбрана сортировка по цене: от большей к меньшей")
else:
    print("Выбрана другая сортировка")

driver.quit()

# 4 Отображение, скидка товара

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

My_Account = driver.find_element_by_id("menu-item-50")
My_Account.click()

Username = driver.find_element_by_id("username")
Username.send_keys("ivanov@email.com")
Password = driver.find_element_by_id("password")
Password.send_keys("7_FJucizqG")
Login = driver.find_element_by_name('login')
Login.click()

Shop = driver.find_element_by_id("menu-item-40")
Shop.click()

driver.execute_script("window.scrollBy(0, 500);")

Android_guide = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
Android_guide.click()

Old_Price = driver.find_element_by_css_selector("del > span")
Old_Price_text = Old_Price.text
assert Old_Price_text == "₹600.00"

New_Price = driver.find_element_by_css_selector("ins > span")
New_Price_text = New_Price.text
assert New_Price_text == "₹450.00"

Img = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
Img.click()
Img_full = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "fullResImage")))
Close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
Close.click()
driver.quit()

# 5 Проверка цены в корзине

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

My_Account = driver.find_element_by_id("menu-item-50")
My_Account.click()

Username = driver.find_element_by_id("username")
Username.send_keys("ivanov@email.com")
Password = driver.find_element_by_id("password")
Password.send_keys("7_FJucizqG")
Login = driver.find_element_by_name('login')
Login.click()

Shop = driver.find_element_by_id("menu-item-40")
Shop.click()

driver.execute_script("window.scrollBy(0, 500);")

HTML5_WebApp = driver.find_element_by_css_selector(".post-182 a[rel='nofollow']")
HTML5_WebApp.click()

time.sleep(2)

Items = driver.find_element_by_class_name("cartcontents")
Items_text = Items.text
assert Items_text == "1 Item"

Sum = driver.find_element_by_css_selector("#wpmenucartli .amount")
Sum_Text = Sum.text
assert Sum_Text == "₹180.00"

View_Basket = driver.find_element_by_class_name("added_to_cart")
View_Basket.click()

Subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "₹180.00"))
Total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Total'] > strong"), "₹183.60"))

driver.quit()

# 6 Работа в корзине

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

Shop = driver.find_element_by_id("menu-item-40")
Shop.click()

driver.execute_script("window.scrollBy(0, 300);")

HTML5_WebApp = driver.find_element_by_css_selector(".post-182 a[rel='nofollow']")
HTML5_WebApp.click()

time.sleep(2)

driver.execute_script("window.scrollBy(0, 600);")

JS_Data = driver.find_element_by_css_selector("[data-product_id='180']")
JS_Data.click()

time.sleep(2)

View_Basket = driver.find_element_by_class_name("added_to_cart")
View_Basket.click()

time.sleep(2)

Delete_1 = driver.find_element_by_css_selector("[data-product_id='182']")
Delete_1.click()

Undo = driver.find_element_by_css_selector(".woocommerce-message a")
Undo.click()

Quantity = driver.find_element_by_css_selector("tbody :nth-child(1) .quantity input")
Quantity.clear()
Quantity.send_keys("3")

Update = driver.find_element_by_name("update_cart")
Update.click()

Quantity_JS = Quantity.get_attribute("value")
assert Quantity_JS == "3"

time.sleep(2)

Apply_Coupon = driver.find_element_by_name("apply_coupon")
Apply_Coupon.click()

Error_Coupon = driver.find_element_by_css_selector(".woocommerce-error li")
Error_Coupon_text = Error_Coupon.text
assert Error_Coupon.text == "Please enter a coupon code."

driver.quit()

# 7 Покупка товара

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

Shop = driver.find_element_by_id("menu-item-40")
Shop.click()

driver.execute_script("window.scrollBy(0, 300);")

HTML5_WebApp = driver.find_element_by_css_selector(".post-182 a[rel='nofollow']")
HTML5_WebApp.click()

View_Basket = driver.find_element_by_class_name("added_to_cart")
View_Basket.click()

Checkout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
Checkout.click()

First_Name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
First_Name.send_keys("Ivan")

Last_Name = driver.find_element_by_id("billing_last_name")
Last_Name.send_keys("Ivanov")

Email = driver.find_element_by_id("billing_email")
Email.send_keys("email@email.com")

Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys("12123342552")

Select_drop = driver.find_element_by_id("s2id_billing_country")
Select_drop.click()

Search_Country = driver.find_element_by_id("s2id_autogen1_search")
Search_Country.send_keys("Russia")

Select_first_counrty = driver.find_element_by_class_name("select2-results-dept-0")
Select_first_counrty.click()

Address = driver.find_element_by_name("billing_address_1")
Address.send_keys("Nevskiy prospect")

driver.execute_script("window.scrollBy(0, 300);")

City = driver.find_element_by_name("billing_city")
City.send_keys("Saint-Petersburg")

Country = driver.find_element_by_name("billing_state")
Country.send_keys("Russia")

Postcode = driver.find_element_by_name("billing_postcode")
Postcode.send_keys("12345-6789")

driver.execute_script("window.scrollBy(0, 600);")

time.sleep(2)

Check_Payments = driver.find_element_by_id("payment_method_cheque")
Check_Payments.click()

driver.execute_script("window.scrollBy(0, 300);")

Place_Holder = driver.find_element_by_id("place_order")
Place_Holder.click()

Thank_You = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

Payment_Method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot :nth-child(3) td"), "Check Payments"))

driver.quit()

