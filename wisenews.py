from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
import re

driver = webdriver.Chrome("C:\\dev\\selenium-sung\\chromedriver.exe")
driver.get('https://login.lib.ezproxy.ust.hk/login?url=http://libwisenews.wisers.net/?gid=HKUST&user=ipaccess&pwd=ipaccess')
while True:
	try:
		driver.find_element_by_name("user").send_keys('jyhong')	
		break;
	except:
		pass
driver.find_element_by_name("pass").send_keys('jean6940',Keys.RETURN)

while True:
	try:
		driver.switch_to_frame("header")	
		break;
	except:
		pass

while True:
	try:
		driver.execute_script('''productChange();''')	
		break;
	except:
		pass
while True:
	try:
		driver.execute_script('''goToSettingPage();''')
		break;
	except:
		pass
while True:
	try:
		driver.switch_to_frame("ws5-content")
		break;
	except:
		pass

while True:
	try:
		driver.find_elements_by_css_selector("""input[type='radio'][value='en-zh_CN']""")[0].click()
		break;
	except:
		pass
driver.execute_script('''changeSetting("ChangeLangForm");''')
print('ok')
while True:
	try:
		driver.switch_to_frame("ws5-content")
		break;
	except:
		pass
while True:
	try:
		driver.find_element_by_xpath("//div[@id='landing_keyword']/input[@type='text']").send_keys("air pollution")#大氣汚染
		break;
	except:
		pass


driver.find_element_by_xpath("//input[@id='datepicker1']").send_keys(Keys.BACKSPACE*10,Keys.DELETE*10)
driver.find_element_by_xpath("//input[@id='datepicker1']").send_keys('2017-01-01')
driver.find_element_by_xpath("//input[@id='datepicker2']").send_keys(Keys.BACKSPACE*10,Keys.DELETE*10)
driver.find_element_by_xpath("//input[@id='datepicker2']").send_keys('2017-12-31')

print("done to here")
driver.find_element_by_xpath("//input[@id='regionSelectAll']").click()
driver.find_element_by_xpath("//input[@id='cn']").click()

driver.find_element_by_xpath("//div[@id='view_media_list']/a").click()
time.sleep(1)

driver.find_element_by_id('tree-publication-region2').click()
driver.find_element_by_id('tree-publication-region2').send_keys(Keys.DOWN*2,Keys.RETURN)
driver.execute_script('''OpenSourceList2();''')

while True:
	try:
		driver.find_element_by_id('0-publicationTreeUI:G>>region=cn')
		break;
	except:
		driver.find_element_by_id('tree-publication-region2').click()
		driver.find_element_by_id('tree-publication-region2').click()
		driver.execute_script('''OpenSourceList2();''')
		time.sleep(0.2)
		pass

driver.find_element_by_id('tree-publication-type2').click()
driver.find_element_by_id('tree-publication-type2').send_keys(Keys.DOWN*1,Keys.RETURN)
driver.execute_script('''OpenSourceList2();''')
# driver.find_element_by_id('tree-publication-search-pattern2').click()
while True:
	try:
		driver.find_element_by_id('0-publicationTreeUI:G>>region=cn>>type=newspaper').click()
		break;
	except:
		driver.find_element_by_id('tree-publication-type2').click()
		driver.find_element_by_id('tree-publication-type2').click()
		driver.execute_script('''OpenSourceList2();''')
		time.sleep(0.2)
		pass
driver.execute_script('''confirmMedia();''')
driver.execute_script('''SubmitSearch();''')
while True:
	try:
		driver.switch_to_frame("result-list")
		break;
	except:
		pass
time.sleep(3)
num_ex = re.compile('[0-9]+')
f = open('output2.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
source = driver.page_source
soup = BeautifulSoup(source,'html.parser')
time.sleep(1)
h = open('page.txt', 'w')
e = source
be = str(e.encode('utf-8'))
h.write(be)
h.close()
# print(soup)
pages = soup.findAll('li', attrs={'class':'pages_links'})
print(type(pages))
print(pages)
page = 1
for pg in pages:
	print('k')
for pg in pages:
	source = driver.page_source
	soup = BeautifulSoup(source,'html.parser')
	time.sleep(1)
	samp_title = soup.findAll('div', attrs={'id':'results_title'})
	samp_date = soup.findAll('div', attrs={'class':'results_date notranslate'})
	samp_resource = soup.findAll('div', attrs={'class':'results_source'})
	samp_section = soup.findAll('div', attrs={'class':'results_section'})
	samp_word = soup.findAll('div', attrs={'class':'results_words notranslate'})#re로 후처리 필요
	samp_link = soup.findAll('div',attrs={'class':'results_type'})
	cnt = 0
	page = page+1
	for i in samp_title:
		title = str(samp_title[cnt].contents[1].contents[0].contents[0])
		date = str(samp_date[cnt].contents[0])
		resource = str(samp_resource[cnt].contents[3].contents[0])
		section = str(samp_section[cnt].contents[1].contents[0])
		words = int(num_ex.findall(str(samp_word[cnt].contents[0]))[0])
		link = str(samp_link[cnt*3].contents[1].get('href')[11:]+';')
		# contents = driver.execute_script(link)
		wr.writerow([date,'',resource,'',section,'',words,'',title,'',link])
		cnt = cnt+1
	# if pg == pages.contents[-1]
		# break
	
	scrp = '//Page '+str(page)
	driver.execute_script(scrp)
	time.sleep(1)
# k = driver.get_attribute('innerHTML')

f.close()
