from selenium import webdriver
from webdriver_manager.chrome  import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains 
from datetime import date
from pathlib import Path
from url1 import URL1
from url2 import URL2
from url3 import URL3
from url4 import URL4
from url5 import URL5
from url6 import URL6


class TestSwag():
   def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(URL1)
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
    

   def teardown(self):
        self.driver.quit()
   
   def waitforelementvisiable(self, selectorType, selector):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((selectorType, selector)))
        return element 
   
    

   def login(self):
        self.waitforelementvisiable(By.ID,'user-name')
        usernameInput = self.driver.find_element(By.ID,'user-name')
        self.waitforelementvisiable(By.ID,'password')
        passwordInput = self.driver.find_element(By.ID,'password')
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn =self.driver.find_element(By.ID,"login-button")
        loginBtn.click() 
        self.driver.get(URL2)
        sleep(2) 
        assert True   

   def test_twGidis(self):
        self.login()
        self.waitforelementvisiable(By.XPATH, "//*[@id='page_wrapper']/footer/ul/li[1]/a")
        twitterButton = self.driver.find_element(By.XPATH,"//*[@id='page_wrapper']/footer/ul/li[1]/a")
        twitterButton.click()
        self.driver.get(URL3)
        sleep(2)
        self.driver.save_screenshot(self.folderPath+"test-twgidis.png")
        assert True

   def test_fbGidis(self): 
        self.login()
        self.waitforelementvisiable(By.XPATH,"//*[@id='page_wrapper']/footer/ul/li[2]/a")
        fbButton = self.driver.find_element(By.XPATH,"//*[@id='page_wrapper']/footer/ul/li[2]/a")
        fbButton.click()
        self.driver.get(URL4)
        self.driver.save_screenshot(self.folderPath+"test-fbgidis.png")
        sleep(2)
        assert True

   def test_lnkdnGidis(self):
        self.login()
        self.waitforelementvisiable(By.XPATH,"//*[@id='page_wrapper']/footer/ul/li[3]/a")
        lnkdnButton = self.driver.find_element(By.XPATH,"//*[@id='page_wrapper']/footer/ul/li[3]/a")
        lnkdnButton.click()
        self.driver.get(URL5)
        self.driver.save_screenshot(self.folderPath+"test-lnkdngidis.png")
        sleep(2)
        assert True

   def test_nameZtoA(self):
        self.login()
        self.waitforelementvisiable(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
        nameButton = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
        nameButton.click()
        nameButton2 = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[2]")
        nameButton2.click()
        self.driver.save_screenshot(self.folderPath+"test-nameZtoA.png")
        sleep(2)
        assert True

   def test_priceLowtoHigh(self):
        self.login()
        self.waitforelementvisiable(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
        nameButton = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
        nameButton.click()
        priceButton1 = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[3]")
        priceButton1.click()
        self.driver.save_screenshot(self.folderPath+"test-nameLowtoHigh.png")
        sleep(2)
        assert True    


   def test_priceHightoLow(self):
        self.login()
        self.waitforelementvisiable(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
        nameButton = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
        nameButton.click()
        priceButton2 = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[4]")
        priceButton2.click()
        self.driver.save_screenshot(self.folderPath+"test-nameHightoLow.png")
        sleep(2)
        assert True    

   def informationcheckout(self):
        self.login()
        self.waitforelementvisiable(By.ID,"add-to-cart-sauce-labs-backpack")
        addProduct1 = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addProduct1.click()
        self.waitforelementvisiable(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
        addProduct2 = self.driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
        addProduct2.click()
        cart =self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cart.click()
        checkoutButton = self.driver.find_element(By.ID,"checkout")
        checkoutButton.click()
        sleep(2)
        assert True

   def test_invalidFname(self):
        self.informationcheckout()
        continueButton = self.driver.find_element(By.ID,"continue")
        continueButton.click()
        errormessage = self.driver.find_element(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
        assert errormessage.text == "Error: First Name is required"
        self.driver.save_screenshot(self.folderPath+"test-invalidFname.png")

   def test_invalidLname(self):
        self.informationcheckout()
        fname= self.driver.find_element(By.ID,"first-name")
        fname.send_keys("abaxbcbcabc")
        continueButton = self.driver.find_element(By.ID,"continue")
        continueButton.click()
        errormessage =self.driver.find_element(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
        assert errormessage.text == "Error: Last Name is required"
        self.driver.save_screenshot(self.folderPath+"test-invalidLname.png")


   def test_invalidPcode(self):
        self.informationcheckout()
        fname= self.driver.find_element(By.ID,"first-name")
        fname.send_keys("abaxbcbcabc")
        lname =self.driver.find_element(By.ID,"last-name")
        lname.send_keys("dkdsdklksvklddksf")
        continueButton = self.driver.find_element(By.ID,"continue")
        continueButton.click()
        errormessage =self.driver.find_element(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
        self.driver.save_screenshot(self.folderPath+"test-invalidPcode.png")
        assert errormessage.text == "Error: Postal Code is required"    
        


   def test_swagAbout(self):
        self.login()
        treeLineButton = self.driver.find_element(By.XPATH,"//*[@id='react-burger-menu-btn']")
        treeLineButton.click()
        wait = WebDriverWait(self.driver,10)       
        aboutButton = wait.until(ec.element_to_be_clickable((By.ID, "about_sidebar_link")))
        aboutButton.click()
        self.driver.get(URL6)
        tryItFree = self.driver.find_element(By.XPATH,"//*[@id='__next']/header/div/div/div[2]/div/div[3]/a/button")
        tryItFree.click()
        self.driver.save_screenshot(self.folderPath+"test-swagabout.png")
        assert True






           
            