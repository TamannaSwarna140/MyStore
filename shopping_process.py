from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from  selenium.webdriver import ActionChains
import time

class ShoppingProcess():
    def shopping_process_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('http://automationpractice.com/index.php')
        time.sleep(3)

        # Sign In button
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)
        # Email
        driver.find_element(By.ID, 'email_create').send_keys('tamannasorna12@gmail.com')
        time.sleep(2)
        # Create Account Button
        driver.find_element(By.XPATH, '//*[@id="SubmitCreate"]/span').click()
        time.sleep(10)
        # Customer First Name
        driver.find_element(By.ID, 'customer_firstname').send_keys('Swarna')
        time.sleep(2)
        # Title
        driver.find_element(By.XPATH, '//*[@id="id_gender2"]').click()
        time.sleep(2)
        # Customer Last Name
        driver.find_element(By.ID,'customer_lastname').send_keys('Akter')
        time.sleep(2)
        # Password
        driver.find_element(By.ID,'passwd').send_keys('11111')
        time.sleep(2)
        # Date of Birth #Day
        day = Select(driver.find_element(By.ID,'days'))
        day.select_by_value('1')
        time.sleep(2)
        # Month
        month = Select(driver.find_element(By.ID,'months'))
        month.select_by_value('10')
        time.sleep(2)
        # Year
        year = Select(driver.find_element(By.ID,'years'))
        year.select_by_value('2000')
        time.sleep(2)
        # CheckBox
        driver.find_element(By.ID,'newsletter').click()
        time.sleep(2)
        #Address
        driver.find_element(By.ID,'address1').send_keys('896 Christy Ridges Suite 534')
        time.sleep(2)
        # City
        driver.find_element(By.ID,'city').send_keys('North Sherwood')
        time.sleep(2)
        # State
        state = Select(driver.find_element(By.ID,'id_state'))
        state.select_by_value('24')
        time.sleep(2)
        # Postal code
        driver.find_element(By.ID,'postcode').send_keys('47232')
        time.sleep(2)
        # Mobile Phone
        driver.find_element(By.ID,'phone_mobile').send_keys('+19898134474')
        time.sleep(2)
        # Register Button
        driver.find_element(By.XPATH,'//*[@id="submitAccount"]/span').click()
        time.sleep(3)
        # Sign Out
        driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[2]/a').click()
        time.sleep(2)

        # Verify Account
        # Insert Email Address
        driver.find_element(By.ID,'email').send_keys('tamannasorna12@gmail.com')
        time.sleep(2)
        # Insert Password
        driver.find_element(By.ID,'passwd').send_keys('11111')
        time.sleep(2)
        # Log In to the System
        driver.find_element(By.XPATH,'//*[@id="SubmitLogin"]/span').click()
        time.sleep(2)
        # T-shirt Section
        driver.find_element(By.XPATH,'//*[@id="block_top_menu"]/ul/li[3]/a').click()
        time.sleep(3)
        # Filtering T-shirts with blue color
        tshirt = driver.find_element(By.XPATH,'//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')
        action = ActionChains(driver)
        action.move_to_element(tshirt).perform()
        time.sleep(5)
        # Click Blue Color
        driver.find_element(By.ID, 'color_2').click()
        time.sleep(5)
        # Add to Cart
        driver.find_element(By.XPATH,'//*[@id="add_to_cart"]/button/span').click()
        time.sleep(3)
        driver.switch_to.default_content()
        time.sleep(3)
        # Check Out
        driver.find_element(By.XPATH,'//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span').click()
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="center_column"]/p[2]/a[1]/span').click()
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="center_column"]/form/p/button/span').click()
        time.sleep(3)
        # Terms of Servic
        driver.find_element(By.ID,'cgv').click()
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="form"]/p/button/span').click()
        time.sleep(3)
        # Selecting Payment Process
        driver.find_element(By.XPATH,'//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a').click()
        time.sleep(3)
        # Order Confirmation
        driver.find_element(By.XPATH,'//*[@id="cart_navigation"]/button/span').click()
        time.sleep(3)

        # Sign Out
        driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[2]/a').click()

        time.sleep(3)

        driver.close()

obj = ShoppingProcess()
obj.shopping_process_demo()

