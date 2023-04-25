import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
from tqdm import tqdm

def drive(url):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # webdriver.Chrome('./chromedriver') #driver 객체 불러옴
    driver.implicitly_wait(3) # 3초 후에 작동하도록
    driver.get(url) #url에 접속
    html = driver.page_source #현재 driver에 나타난 창의 page_source(html) 가져오기
    soup = BeautifulSoup(html, 'lxml') #html 파싱(parsing)을 위해 BeautifulSoup에 넘겨주기
    return driver, soup

def get_soup(driver, nscroll = 3):
        # body = driver.find_element_by_tag_name('body')
        num_page_down = nscroll
        last_height = driver.execute_script("return document.body.scrollHeight") 
        while num_page_down:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            new_height = driver.execute_script("return document.body.scrollHeight")
            # body.send_keys(Keys.PAGE_DOWN)
            
            time.sleep(1.2)
            if new_height == last_height:                                                
                break
            last_height = new_height
            num_page_down -= 1
            
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        return soup