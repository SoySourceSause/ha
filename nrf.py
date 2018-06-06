# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:17:41 2018

@author: plandat
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
####################################################################
PATH_TO_CHROME_DRIVER = "C:\chromedriver_selenuim\chromedriver.exe"
OUT_PUT_FILE_NAME = 'output.csv'
####################################################################


def division(divide):

	while True:
		source = driver.page_source
		soup = BeautifulSoup(source,'html.parser')
		s_chief_of_research = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_10_'})
#		s_year = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_0_'})
#		s_research_serial = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_1_'})
#		s_large_scale_classification = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_4_'})
#		s_medium_scale_classification = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_5_'})
#		s_small_scale_classification = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_6_'})
##		s_very_small_scale_classification = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_7_'})
#		s_research = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_8_'})
#		s_chief_of_research = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_10_'})
#		s_managing_department = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_12_'})

		if (s_chief_of_research != []):
			
			break	
	cnt = 0 
	print("@@@@@@@@@@@@@@")
	s_chief_of_research = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_10_'})
	s_year = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_0_'})
	s_research_serial = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_1_'})
	s_large_scale_classification = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_4_'})
	s_medium_scale_classification = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_5_'})
	s_small_scale_classification = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_6_'})
	s_very_small_scale_classification = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_7_'})
	s_research = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_8_'})
	s_chief_of_research = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_10_'})
	s_managing_department = soup.findAll('td', attrs={'class':'grid_body_column grid_body_column_data grid1_columnstyle_12_'})


	time.sleep(0.3)
    
        

 
	for i in s_chief_of_research:
		chief_of_research = str(s_chief_of_research[cnt].contents[0].contents[0])
		cnt2 = 0
		year = str(s_year[cnt].contents[0].contents[0])
		research_serial = str(s_research_serial[cnt].contents[0].contents[0])
		large_scale_classification = str(s_large_scale_classification[cnt].contents[0].contents[0])
		medium_scale_classification = str(s_medium_scale_classification[cnt].contents[0].contents[0])
		small_scale_classification = str(s_small_scale_classification[cnt].contents[0].contents[0])
		very_small_scale_classification = str(s_very_small_scale_classification[cnt].contents[0].contents[0])
		research = str(s_research[cnt].contents[0].contents[0].contents[0])
		managing_department = str(s_managing_department[cnt].contents[0].contents[0])
		
		wr.writerow([year,'',research_serial,'',large_scale_classification,'',medium_scale_classification,'',small_scale_classification,'',very_small_scale_classification,'',research,'',chief_of_research,'',managing_department])
		cnt = cnt+1
		cnt2 += 1
		if cnt == 19:
			return str(s_chief_of_research[0].contents[0])
            

       
print("start")	
driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)# 웹 드라이버 path
driver.get('http://www.nrf.re.kr/biz/doc/new/view?menu_no=50')


while True:
	try:
		driver.switch_to_frame("reframe")
		break
	except:
		time.sleep(0.1)
		pass
time.sleep(10)
driver.find_element_by_xpath("""//*[@id="totalPageSelect_button"]""").click()
target = driver.find_element_by_xpath("""//*[@id="totalPageSelect_itemTable_6"]""")



while True:
	try:    
		target.click()
		break
	except:
		time.sleep(1)
		pass
time.sleep(10)

num_ex = re.compile('[0-9]+')
f = open(OUT_PUT_FILE_NAME, 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
time.sleep(4)


while True:
	source = driver.page_source
	soup = BeautifulSoup(source,'html.parser')
	pages = soup.findAll('td', attrs={'class':'w2pageList_col_label'})
	if pages != []:
		break
	else:
		print('page not loaded please restart')
		time.sleep(0.1)

check = 0
page = 6
for a in range(7):#1~7page

	divide = 527
	window_before = driver.window_handles[0]
	result_div = []
	while divide:
		result_div.insert(divide, division(divide))
		cell = driver.find_element_by_xpath("""//*[@id="grid1_cell_19_4"]""")
		actions = ActionChains(driver)#.키나 클릭입력을 애가 튕겨낼때는 actionchains사용. 더블클릭에도 사용
		actions.move_to_element(cell)
		actions.double_click(cell)
		actions.perform()
		time.sleep(0.1)

		actions.send_keys(Keys.DOWN*19).perform()
		time.sleep(1)

		time.sleep(0.4)
		divide -= 1

	driver.find_element_by_xpath("""//*[@id="pageList1_next_btn"]""").click()
	time.sleep(3)

#마지막 페이지

divide = 527
while divide:
	result_div.insert(divide, division(divide))
	cell = driver.find_element_by_xpath("""//*[@id="grid1_cell_19_4"]""")
	actions = ActionChains(driver)#.키나 클릭입력을 애가 튕겨낼때는 actionchains사용. 더블클릭에도 사용
	actions.move_to_element(cell)
	actions.double_click(cell)
	actions.perform()
	time.sleep(0.1)
#		act.move_to_element(driver.find_element_by_xpath("""//*[@id="grid1_cell_0_4"]/nobr""")).click()
	actions.send_keys(Keys.DOWN*19).perform()
	time.sleep(1)
#		if divide != 5:
#			print(result_div[divide])
#			print(result_div[divide + 1])
#			if result_div[divide] == result_div[divide + 1]:
#				break
	time.sleep(0.4)
	divide -= 1
	
#	samp_date = soup.findAll('div', attrs={'class':'results_date notranslate'})
#	samp_resource = soup.findAll('div', attrs={'class':'results_source'})
#	samp_section = soup.findAll('div', attrs={'class':'results_section'})
#	samp_word = soup.findAll('div', attrs={'class':'results_words notranslate'})
#	samp_link = soup.findAll('div',attrs={'class':'results_type'})


f.close()