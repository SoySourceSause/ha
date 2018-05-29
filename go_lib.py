# -*- coding: utf-8 -*-
"""
Created on Tue May 29 01:25:23 2018

@author: plandat
"""
from html.parser import HTMLParser
import requests
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import threading
import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json

class go_lib:
    def __init__(self):        
        self.driver =  webdriver.Chrome("C:\chromedriver_selenuim\chromedriver.exe");        
        self.driver.get("https://login.lib.ezproxy.ust.hk/login?url=http://libwisenews.wisers.net/?gid=HKUST&user=ipaccess&pwd=ipaccess")
        
    def login(self, id, password):
         
        self.driver.find_element_by_xpath("""//*[@id="EntireBody"]/form/table[2]/tbody/tr[1]/td[2]/input""").send_keys(id)
        self.driver.find_element_by_xpath("""//*[@id="EntireBody"]/form/table[2]/tbody/tr[3]/td[2]/input""").send_keys(password)
        self.driver.find_element_by_xpath("""//*[@id="EntireBody"]/form/table[2]/tbody/tr[4]/td[2]/input""").click()
        time.sleep(0.2)
   
    
    def clicking(self):
        self.driver.switch_to_frame("header")
        self.driver.find_element_by_xpath("""/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[2]/a""").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("""//*[@id="nav-8"]""").click() #setting click
        time.sleep(3)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("ws5-content")
        time.sleep(7)
        self.driver.find_element_by_xpath("""//*[@id="language-selection-layer"]/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/span/input""").click()
        self.driver.find_element_by_xpath("""//*[@id="language-selection-layer"]/form/table/tbody/tr[2]/td/input[2]""").click() #save
    def keyword(self, key_word, date_start, date_end):
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("ws5-content")
        time.sleep(0.3)
        self.driver.find_element_by_xpath("""//*[@id="searchTxt"]""").send_keys(key_word)
        print("I'm here")
        self.driver.find_element_by_xpath("""//*[@id="datepicker1"]""").send_keys(Keys.CONTROL + "a", Keys.DELETE)
        self.driver.find_element_by_xpath("""//*[@id="datepicker1"]""").send_keys(date_start)
        self.driver.find_element_by_xpath("""//*[@id="datepicker2"]""").send_keys(Keys.CONTROL + "a", Keys.DELETE)
        self.driver.find_element_by_xpath("""//*[@id="datepicker2"]""").send_keys(date_end)
        time.sleep(0.1)
        self.driver.find_element_by_xpath("""//*[@id="regionSelectAll"]""").click()
        time.sleep(0.2)
        self.driver.find_element_by_xpath("""//*[@id="cn"]""").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("""//*[@id="view_media_list"]/a""").click()#media
        time.sleep(4)
        self.driver.find_element_by_xpath("""//*[@id="tree-publication-region2"]""").send_keys("Mainland China")
        time.sleep(1.5)
        self.driver.find_element_by_xpath("""//*[@id="tree-publication-type2"]""").send_keys("Newspaper")
        time.sleep(1.5)
        self.driver.find_element_by_xpath("""//*[@id="search-sourceList-button2"]""").click
   #     time.sleep(1)
    #    self.driver.find_element_by_xpath("""//*[@id="0-publicationTreeUI:G>>region=cn>>type=newspaper"]""").click()
        trying = 0
        while trying <=30:
            try:
                time.sleep(0.1)                
                self.driver.find_element_by_xpath("""//*[@id="0-publicationTreeUI:G>>region=cn>>type=newspaper"]""").click()
                time.sleep(0.1)
                trying = 101
            except:
                print("no")
                trying += 1
                time.sleep(0.1)
                print("yes")
        time.sleep(1)
        self.driver.find_element_by_xpath("""//*[@id="sourcelisting"]/div[5]/div[2]/a[2]/div""").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("""//*[@id="search_en"]""").click()
     
    def crawling(self):
        time.sleep(10)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        #url = self.driver.page_source
        #time.sleep(0.2)
        print("아")
        #print(url)
        time.sleep(0.2)
        #res = requests.get(url) ->로그인때문인지 뭔지 안됨
        #self.driver.get("http://libwisesearch.wisers.net.lib.ezproxy.ust.hk/wortal/index.do?srp_restore&switch-product=true&currentsubdb=")
        time.sleep(30)
        html = self.driver.page_source
        
        time.sleep(0.2)
        print("에")
     #   time.sleep(30)
       ## soup = BeautifulSoup(html,'html.parser')
        soup = BeautifulSoup(html,'lxml')
        
        print("이")
        time.sleep(2)
        #이거 표기법 바꿔서 다시해보기-> 안된다
#  ㅇ      hi = soup.select('.result')
 #   ㅇ    hello = soup.select('.tabcontent')
  #    ㅇ  hoa = soup.select('.headline_read')
        
        hello = soup.select("span", "headline_read")
        hoaa = soup.find_all('div', id = 'results_title')
        hoa = soup.find_all('span')
        hoa
        #text_please = [hoaa[n].find('a').get_text() for n in range(0,hoaa)]
        #text_please
        
        #results_title = soup.select('.headline_read')
        print("오")
        
        print("hi")
        print(hello)
        print("hello")
        print(hoa)
        print("hoa")
        print(hoaa)
        for h in hoa:
            print(h.text.strip())
        hi = soup.select('a')
        
        print(hi)
        
       # print(hoa.text)
       # print(results_title)
       # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
        #print(results_title)
        #soup.find_all('a')
        #print(results_title_a.get_text())
                                   
        
        
       #url 복사떠서 해보기->안됨
        
        
k = go_lib()
k.login("jyhong","jean6940")
time.sleep(2)
k.clicking()
time.sleep(10)
k.keyword("空气污染", "2017-01-01", "2017-12-31")
#k.keyword("대기오염")
k.crawling()
    
    
    
