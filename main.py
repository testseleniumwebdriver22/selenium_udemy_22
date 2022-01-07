from selenium import webdriver
import os
import time
import psycopg2
from dbconnect import DbConnect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
from apscheduler.schedulers.blocking import BlockingScheduler

class MainTest():
 
 def __init__(self,incrementing_each_time,already_done):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
        DATABASE_URI = os.environ.get("DATABASE_URL")
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)


        site="https://www.pionex.com/en-US/market"
        
        driver.get(site)
        
        delay = 60 # seconds
        
        path="//*[contains(@class,'tableRow___w5YrW')]"
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,path)))
            print ("Page is ready!")
            
        except TimeoutException:
            print ("Loading took too much time!")
            driver.close()
            driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
            driver.get(site)
            
        driver.execute_script("document.getElementsByClassName('table-container___8a_Yd')[0].style.height='16800px';") 
        
        i=0
        while(i<2):
         
            elements = driver.find_elements_by_xpath("//*[contains(@class,'tableRow___w5YrW')]")
       
            print(elements)
            for element in elements:          
                              try:
                                
                                all_list=element.text
                                list_cleaned=all_list.split("\n")
                                crypto_split=list_cleaned[0].split("/")
                                print(crypto_split[0])
                                print(list_cleaned)
                                if crypto_split[0]!="1INCH" and crypto_split[0]!="FOR" and crypto_split[0]!="ANY":
                                 dbc=DbConnect()
                                 dbc.create_table_crypto_value(str(crypto_split[0]))
                                 dbc.check_if_full(str(crypto_split[0]))  
                                 dbc.fill_table(str(crypto_split[0]),list_cleaned[2])
    
                                 dbc.pick_from_table_check(crypto_split[0])

                                 dbc.close()
                              except exceptions.StaleElementReferenceException:
                                print("the crypto monitoring procedure is not working")

            i=i+1
            time.sleep(260)
            
    

        driver.close()
            
if __name__ == "__main__":
   incrementing_each_time=28
   already_done=0
   MainTest(incrementing_each_time,already_done)
