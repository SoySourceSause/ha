from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
import re
##############################################
THING_TO_SEARCH = '空气污染'
PATH_TO_CHROME_DRIVER = "D:\\coldreason\\dev\\selenium-sung\\chromedriver.exe"
ID = 'jyhong'
PWD = 'jean6940'
OUT_PUT_FILE_NAME = 'output6.csv'
PERIOD_START = '2017-01-01'
PERIOD_END = '2017-12-31'
##############################################
def contentadvisor(webcontent,outputstring):
	try:
		res = webcontent.contents
		for k in res:
			outputstring = contentadvisor(outputstring, k)
	except:
		try:
			outputstring = outputstring + webcontent.text
		except :
			outputstring = outputstring + webcontent			
	return outputstring

driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)# 웹 드라이버 path
driver.get('https://login.lib.ezproxy.ust.hk/login?url=http://libwisenews.wisers.net/?gid=HKUST&user=ipaccess&pwd=ipaccess')
while True:
	try:
		driver.find_element_by_name("user").send_keys(ID)	
		break;
	except:
		time.sleep(0.1)
		pass
driver.find_element_by_name("pass").send_keys(PWD,Keys.RETURN)
while True:
	try:
		driver.switch_to_frame("header")	
		break;
	except:
		time.sleep(0.1)
		pass
while True:
	try:
		driver.execute_script('''productChange();''')	
		break;
	except:
		time.sleep(0.1)
		pass
while True:
	try:
		driver.execute_script('''goToSettingPage();''')
		break;
	except:
		time.sleep(0.1)
		pass
while True:
	try:
		driver.switch_to_frame("ws5-content")
		break;
	except:
		time.sleep(0.1)
		pass
while True:
	try:
		driver.find_elements_by_css_selector("""input[type='radio'][value='en-zh_CN']""")[0].click()
		break;
	except:
		time.sleep(0.1)
		pass
driver.execute_script('''changeSetting("ChangeLangForm");''')
while True:
	try:
		driver.switch_to_frame("ws5-content")
		break;
	except:
		time.sleep(0.1)
		pass
while True:
	try:
		driver.find_element_by_xpath("//div[@id='landing_keyword']/input[@type='text']").send_keys(THING_TO_SEARCH)#大氣汚染
		break;
	except:
		time.sleep(0.1)
		pass
driver.find_element_by_xpath("//input[@id='datepicker1']").send_keys(Keys.BACKSPACE*10,Keys.DELETE*10)
driver.find_element_by_xpath("//input[@id='datepicker1']").send_keys(PERIOD_START)
driver.find_element_by_xpath("//input[@id='datepicker2']").send_keys(Keys.BACKSPACE*10,Keys.DELETE*10)
driver.find_element_by_xpath("//input[@id='datepicker2']").send_keys(PERIOD_END)
driver.find_element_by_xpath("//input[@id='regionSelectAll']").click()
driver.find_element_by_xpath("//input[@id='cn']").click()
driver.find_element_by_xpath("//div[@id='view_media_list']/a").click()

while True:
	try:
		driver.find_element_by_id('tree-publication-region2').click()
		break;
	except:
		time.sleep(0.1)
		pass
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
		time.sleep(0.1)
		pass
driver.find_element_by_id('tree-publication-type2').click()
driver.find_element_by_id('tree-publication-type2').send_keys(Keys.DOWN*1,Keys.RETURN)
driver.execute_script('''OpenSourceList2();''')
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
		time.sleep(0.1)
		pass
num_ex = re.compile('[0-9]+')
f = open(OUT_PUT_FILE_NAME, 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
time.sleep(4)
while True:
	source = driver.page_source
	soup = BeautifulSoup(source,'html.parser')
	last_page = soup.findAll('li', attrs={'id':'pages_input'})
	if last_page != []:
		break
	else:
		print('page not loaded please restart')
		time.sleep(0.1)
last_page = int(num_ex.findall(last_page[0].contents[-1].contents[0])[0])
for pg in range(2,last_page+2):
	window_before = driver.window_handles[0]
	while True:
		source = driver.page_source
		soup = BeautifulSoup(source,'html.parser')
		samp_title = soup.findAll('div', attrs={'id':'results_title'})
		if samp_title != []:
			break	
	samp_date = soup.findAll('div', attrs={'class':'results_date notranslate'})
	samp_resource = soup.findAll('div', attrs={'class':'results_source'})
	samp_section = soup.findAll('div', attrs={'class':'results_section'})
	samp_word = soup.findAll('div', attrs={'class':'results_words notranslate'})
	samp_link = soup.findAll('div',attrs={'class':'results_type'})
	cnt = 0
	for i in samp_title:
		title = str(samp_title[cnt].contents[1].contents[0].contents[0])
		date = str(samp_date[cnt].contents[0])
		resource = str(samp_resource[cnt].contents[3].contents[0])
		section = str(samp_section[cnt].contents[1].contents[0])
		words = int(num_ex.findall(str(samp_word[cnt].contents[0]))[0])
		link = str(samp_link[cnt*3].contents[1].get('href')[11:]+';')
		stringd = ''
		try:
			driver.execute_script(link)
			window_after = driver.window_handles[1]
			driver.switch_to_window(window_after)
			while True:
				indivi_page = driver.page_source
				indivi_src = BeautifulSoup(indivi_page,'html.parser')
				title_n = indivi_src.findAll('span', attrs={'class':'bluebold'})
				if title_n != []:
					break
				else :
					time.sleep(0.2)
			title = contentadvisor(title_n[0],'')
			driver.switch_to_window(window_before)
			while True:
				try:
					driver.switch_to_default_content()
					break;
				except:
					time.sleep(0.2)
					pass
			driver.switch_to_frame("ws5-content")
			k = indivi_src.findAll('td',attrs={'class':'content'})
			stringd = ''
			stringd = contentadvisor(k[0],stringd).strip()
			driver.switch_to_frame("result-list")
		except:
			pass
		wr.writerow([date,'',resource,'',section,'',words,'',title,'',stringd])
		cnt = cnt+1
	
	if(pg != last_page+1):
		scrp = "SubmitWithRewriteURL('" + str(pg) + "');" 
		driver.execute_script(scrp)
		time.sleep(4)
	msg = str(pg-1) +'/'+ str(last_page) + ' done'
	print(msg)
f.close()
