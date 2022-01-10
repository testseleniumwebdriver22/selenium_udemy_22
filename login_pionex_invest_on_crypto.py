# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from PIL import Image
from io import BytesIO
import time
from image_rec import Image_rec
import numpy as np
import re
import random
import os
import cloudinary as cloudinary
import cloudinary.uploader
from email_verification import Get_Emails


class Login_Pionex_Invest_On_Crypto:

  def __init__(self,crypto_name_to_invest,amount_to_invest):              
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
    DATABASE_URI = os.environ.get("DATABASE_URL")

    # def load_driver():
    #   options = webdriver.FirefoxOptions()
      
    #   # enable trace level for debugging 
    #   #options.log.level = "trace"

    #   #options.add_argument("-remote-debugging-port=9224")
    #   options.add_argument("-headless")
    #   #options.add_argument("-disable-gpu")
    #   #options.add_argument("-no-sandbox")

    #   binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

    #   firefox_driver = webdriver.Firefox(
    #     firefox_binary=binary,
    #     executable_path=os.environ.get('GECKODRIVER_PATH'),
    #     options=options)

    #   return firefox_driver
    
    
    site="https://www.pionex.com/en-US/sign"
    # self.driver = load_driver()
    # self.driver.get(site)
    
    self.delay=30
    
    self.crypto_name_to_invest=crypto_name_to_invest
    self.amount_to_invest=amount_to_invest
    
    self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    self.driver.get(site)
        
    
    self.driver.find_element_by_xpath("//*[contains(@class,'inputContainer___88mru')]//input[@placeholder='Phone number / Email']").send_keys("testseleniumwebdriver22@gmail.com")
    
    self.driver.find_element_by_xpath("//*[contains(@class,'inputContainer___88mru')]//input[@placeholder='Password']").send_keys("testselenium22")
        
    self.driver.find_element_by_xpath("//*[contains(@class,'ant-btn t-button signBtn___1i0eQ ant-btn-primary')]").click()
    
        
    class_name="geetest_slider_button"
    
    try:
                 myElem = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.CLASS_NAME,class_name)))
                 print ("Slider is shown up!")
                
    except TimeoutException:
                print ("slider not coming up, intelligent verification not required!")
                time.sleep(15)
                self.get_and_insert_verification_code()
                

  def get_and_insert_verification_code(self):
                try:
                 myElem = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH,"//*[contains( text(), 'CONFIRM')]")))
                 print ("verification code requested")
                
                except TimeoutException:
                  print ("verification code window not shown up")
    
                get_emailsobj=Get_Emails()
                self.verification_code=get_emailsobj.get_verification_code()
                print("verification code is: "+self.verification_code)
                input_ver_code=self.driver.find_element_by_xpath("//*[contains(@id,'rcDialogTitle2')]//*input")
                print(str(input_ver_code.get_attribute("outerHTML")))
                input_ver_code.send_keys(str(self.verification_code))
                #self.save_screenshot()
                time.sleep(2)
                
                print("verification code correctly inserted")
                self.save_screenshot()
                               

                class_name="ant-modal-confirm-content"
    
    
                try:
                  myElem = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.CLASS_NAME,class_name)))
                  print ("Login success!")
                
                
                except TimeoutException:
                  print ("Login not success...")

  def update_cursor_position(self):
      regex = re.compile(r'(\w*)px')
      string=self.driver.find_element_by_xpath("//*[contains(@class,'geetest_slider_button')]").get_attribute("style")
      match = re.search(regex, string)
      word = match.group(1)
      self.current_slider_pos=int(word)
      
  def Invest_on_crypto(self):
    time.sleep(5)
    self.driver.find_element_by_xpath("//*[contains( text(), 'Market')]").click()
    print("investment phase is beginning....")
    time.sleep(2)
    self.driver.execute_script("document.getElementsByClassName('table-container___8a_Yd')[0].style.height='16850px';") 
    self.driver.find_element_by_xpath("//*[contains(@class,'tableRow___w5YrW ')]//*[contains( text(), '"+self.crypto_name_to_invest+"')]").click() 
    time.sleep(4)
    self.driver.find_element_by_xpath("//*[contains(@id,'rc-tabs-1-tab-manual')]").click() 
    time.sleep(3)
    self.driver.find_element_by_xpath("//*[contains(@class,'container___155fZ')]//*[contains( text(), 'Market')]").click()
    
    self.driver.find_element_by_xpath("//*[contains(@class,'ant-input-number-input-wrap')]//input").send_keys(str(self.amount_to_invest)) 
    self.driver.find_element_by_xpath("//*[contains(@class,'button-trading-up pionex-trading-up-bg')]").click() 
    print("invested on crypto "+self.crypto_name_to_invest+"!!!!")

  
  def save_screenshot(self):
      png = self.driver.get_screenshot_as_png() # saves screenshot of entire page
            
      im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

      im.save('screenshot.png') # saves new cropped image
      
      cloudinary.config( 
        cloud_name = "hjlddlnbw", 
        api_key = "818456115398256", 
        api_secret = "_n-I7r41_dr_15ssHLRvsFCFDp0" 
      )
      cloudinary.uploader.upload("screenshot.png")
   

  def attempt_login(self):  
    
    time.sleep(3)
    element=self.driver.find_element_by_xpath("//*[contains(@class,'geetest_canvas')]")
    
    location = element.location
    size = element.size
    png = self.driver.get_screenshot_as_png() # saves screenshot of entire page
      
      
    im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
     
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
      
    cloudinary.config( 
        cloud_name = "hjlddlnbw", 
        api_key = "818456115398256", 
        api_secret = "_n-I7r41_dr_15ssHLRvsFCFDp0" 
      )

      
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png') # saves new cropped image
      
    cloudinary.uploader.upload("screenshot.png")
    
    
    
   ####################################################################################################################################################  
  
    img_rec=Image_rec()
      
    slide_amount=img_rec.get_slide_quantity()    
    for k in range(1,7):
     
     if slide_amount%k==0:
       i=slide_amount/k
       number_of_movements=k
       
    element=self.driver.find_element_by_xpath("//*[contains(@class,'geetest_slider_button')]")

    correction=0
    def slider_movement(correction): 
     time.sleep(2)
     j=0
     self.update_cursor_position()
     while(self.current_slider_pos<slide_amount): 
        
        print("slide amount"+str(slide_amount))
        print("i= "+str(i))
    
        if slide_amount-self.current_slider_pos>=i:
            element=self.driver.find_element_by_xpath("//*[contains(@class,'geetest_slider_button')]")
            action = webdriver.ActionChains(self.driver)
            element_locating=action.move_to_element(element)
            element_clicked=element_locating.click_and_hold()
            element_clicked.move_by_offset(i, 10).perform()
            
            self.update_cursor_position()
            print("current slider pos after i movement"+str(self.current_slider_pos))
            if(slide_amount%i==0):
             j=j+1
            if(j==number_of_movements):
                element_clicked.release().perform()
                print("element release")
                self.save_screenshot()
                break
                
           
        
        # if slide_amount-self.current_slider_pos<i:
                  
        #           self.update_cursor_position()
        #           #element2=self.driver.find_element_by_xpath("//*[contains(@class,'geetest_slider_button')]")
        #           webdriver.ActionChains(self.driver).move_to_element(element).click_and_hold().move_by_offset(int(slide_amount)-self.current_slider_pos+correction, 10).release().perform()
                                
        #           print("slide_amount-self.current_slider_pos= "+str(type(slide_amount-self.current_slider_pos)))
                                    
        #           element_locating.reset_actions()
                  
        #           self.update_cursor_position()
        #           print("current slider pos after a very small movement"+str(self.current_slider_pos))
                  
                  
                  
        
        time.sleep(random.uniform(1.534,2.3423))
    
    
    slider_movement(correction)          
                            
     
    
    class_name="ant-modal-confirm-content"
    self.save_screenshot()
      

    time.sleep(1)
        
    self.save_screenshot()
    
    print("waiting for the verification code ..")
    
    self.get_and_insert_verification_code()
    # try:
    #              myElem = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.CLASS_NAME,class_name)))
    #              print ("Login success!")
    #              self.Invest_on_crypto()
            
                
    # except TimeoutException:
    #              print ("Login not success, retrying..")
    #              #self.driver.find_element_by_xpath("//*[contains(@class,'geetest_refresh_1')]").click()
    #              #self.attempt_login()
    #              self.driver.close()
    #              login_pionex2=Login_Pionex_Invest_On_Crypto(self.crypto_name_to_invest,self.amount_to_invest)
    #              login_pionex2.attempt_login()

  def driver_close(self):
    self.driver.close()               

  
login_pionex=Login_Pionex_Invest_On_Crypto("ETH",22)
login_pionex.attempt_login()
login_pionex.driver_close()
    


