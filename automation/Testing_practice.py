import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains

class Automation():
    def automation_practice(self):


        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('http://automationpractice.com/index.php')
        driver.maximize_window()
        time.sleep(2)



        sign_in = driver.find_element(By.LINK_TEXT,'Sign in')
        sign_in.click()
        time.sleep(2)

        #Creating account

        email = driver.find_element(By.ID,'email_create')
        email.send_keys('trjuned1@gmail.com')


        createaccountBtn = driver.find_element(By.CSS_SELECTOR, '#SubmitCreate > span')
        createaccountBtn.click()
        time.sleep(5)

        title = driver.find_element(By.CSS_SELECTOR, '#id_gender1')
        title.click()

        fname = driver.find_element(By.ID, 'customer_firstname')
        fname.send_keys("Tazan")
        time.sleep(2)

        lname = driver.find_element(By.ID, 'customer_lastname')
        lname.send_keys("Rabbani")
        time.sleep(2)

        apassword = driver.find_element(By.ID, 'passwd')
        apassword.send_keys("12345678")
        time.sleep(2)

        address = driver.find_element(By.ID, 'address1')
        address.send_keys("Mirpur, Dhaka, 1207.")
        time.sleep(2)

        city = driver.find_element(By.ID, 'city')
        city.send_keys("Dhaka")
        time.sleep(2)

        State = driver.find_element(By.ID, "id_state")
        all_State = Select(State)
        all_State.select_by_index(4)

        zip = driver.find_element(By.ID, 'postcode')
        zip.send_keys("12088")
        time.sleep(2)

        phone = driver.find_element(By.ID, 'phone_mobile')
        phone.send_keys("+880 1754029357")
        time.sleep(2)

        register = driver.find_element(By.CSS_SELECTOR, '#submitAccount > span')
        register.click()
        print(driver.title)
        signout = driver.find_element(By.CSS_SELECTOR, '#header > div.nav > div > div > nav > div:nth-child(2) > a')
        signout.click()
        time.sleep(2)


    # login
#    @pytest.yield_fixture()
    def login(self):
        # global driver
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get('http://automationpractice.com/index.php')
            driver.maximize_window()
            time.sleep(2)

            sign_in = driver.find_element(By.LINK_TEXT, 'Sign in')
            sign_in.click()
            time.sleep(2)

            email_login = driver.find_element(By.ID,'email')
            email_login.send_keys('trjuned2@gmail.com')
            password = driver.find_element(By.ID,'passwd')
            password.send_keys('12345678')
            btn_signin = driver.find_element(By.XPATH,'//*[@id="SubmitLogin"]/span')
            btn_signin.click()

        #t-shirt section
            t_shirt_field = driver.find_element(By.XPATH,'//*[@id="block_top_menu"]/ul/li[3]/a')
            t_shirt_field.click()

            filter_blue = driver.find_element(By.ID,'layered_id_attribute_group_14')
            filter_blue.click()


            actions = ActionChains(driver)

            addtocarthover = driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/span/span')
            actions.move_to_element(addtocarthover).perform()

            addtocart = driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]/span')
            addtocart.click()
            time.sleep(10)
            print(driver.title)
            proceed_to_checkout = driver.find_element(By.XPATH,'//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')
            proceed_to_checkout.click()
            time.sleep(5)

            proceed_to_checkout2 = driver.find_element(By.XPATH,'//*[@id="center_column"]/p[2]/a[1]/span')
            proceed_to_checkout2.click()

            proceed_to_checkout3 = driver.find_element(By.XPATH,'//*[@id="center_column"]/form/p/button/span')
            proceed_to_checkout3.click()
            agree_term = driver.find_element(By.XPATH,'//*[@id="form"]/div/p[2]/label')
            agree_term.click()

            proceed_to_checkout4 = driver.find_element(By.XPATH,'//*[@id="form"]/p/button/span')
            proceed_to_checkout4.click()

            time.sleep(2)
            payment_by_check = driver.find_element(By.XPATH,'//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a/span')
            payment_by_check.click()
            time.sleep(2)

            confirm_order = driver.find_element(By.XPATH,'//*[@id="cart_navigation"]/button/span')
            confirm_order.click()

            #sign out
            sign_out = driver.find_element(By.LINK_TEXT,'Sign out')
            sign_out.click()
            time.sleep(5)

            driver.close()

#def test_login_001_valid(automation_practice):
#    email_login = driver.find_element(By.ID, 'email')
#    password = driver.find_element(By.ID, 'passwd')
#    btn_signin = driver.find_element(By.XPATH, '//*[@id="SubmitLogin"]/span')

#    email_login.send_keys('abc@gmail.com')
#    password.send_keys('12345678')
#    btn_signin.click()



obj = Automation()
obj.automation_practice()
obj.login()

