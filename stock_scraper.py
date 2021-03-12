import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver.exe")

def extract_stocks(stock, start_date, end_date):
	driver.get("https://www.finance.yahoo.com")
	
	elem = driver.find_element_by_name("yfin-usr-qry")
	elem.send_keys(stock)
	time.sleep(10)
	
	elem.send_keys(Keys.RETURN)
	
	url = driver.current_url
	print(f'url {url}')
	
	stockspage = requests.get(url)
	
	if stockspage.status_code != 200:
		return "There was a problem accessing the page"
	
	stockspage_content = stockspage.content
	soup = BeautifulSoup(stockspage.content, 'html.parser')
	low = soup.find_all('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'})[0]
	print(f'low {low}')
	
	current = soup.find_all('td', {'data-test': 'DAYS_RANGE-value'})[0]
	print(f'current {current}')
		
	'''if current <= low:
		print(f'The current stock price is lower than the 52 week low at {current} vs low {low}')
	else:
		print(f'The current stock price is higher than the 52 week low at {current} vs low {low}')'''
		
	'''with open(stock + '_prices.txt', 'wb') as f:
		f.write(soup.prettify().encode('utf-8'))
	f.close()'''
	
def get_site(site):
	website = requests.get(site)
	if website.status_code != 200:
		return "There was a problem accessing the page"
	soup = BeautifulSoup(website.content, 'html.parser')
	with open('site_content.txt', 'wb') as f:
		f.write(soup.prettify().encode('utf-8'))
	f.close()
	
if __name__=='__main__':
	stock = 'shop'
	#stock = 'baba'
	#stock = 'etsy'
	#stock = 'amz'
	#stock = 't' #att
	#stock = 'low'
	#stock = 'wmt'
	
	start_date = '2019-06-01'
	end_date = '2020-06-01'
	
	extract_stocks(stock, start_date, end_date)
	site = 'https://www.google.com'
	#get_site(site)
