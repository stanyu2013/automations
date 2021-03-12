import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver.exe")

def extract_news(category):

	driver.get("https://www.google.com")
	elem = driver.find_element_by_name("q")
	elem.send_keys(category)
	elem.send_keys(Keys.ENTER)
	
	news = driver.find_element_by_xpath("//a[@class='q qs'][1]")
	news.click()
	
	page = 1
	
	save_news(page)
	
	while True:
		try:
			page += 1
			save_news(page)
			driver.find_element_by_xpath("//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()
		except:
			driver.close()
			
def save_news(page):
	#driver.switch_to_window(driver.window_handles[-1])
	url = driver.current_url
	
	# Tag, NavigableString, BeautifulSoup, Comment
	#newspage = requests.get("https://www.cnn.com")
	
	newspage = requests.get(url)
	
	if newspage.status_code != 200:
		return "There was a problem accessing the page"
	
	soup = BeautifulSoup(newspage.content, 'html.parser')
	
	with open(category+'_filtered.txt', 'wb') as f:
		f.write(soup.prettify().encode('utf-8'))
		
	category_news = soup.find_all(class_='BNeawe vvjwJb AP7Wnd')
		
	#li = soup.find_all('div', {'class': 'kCrYT'})
	li = soup.find_all('div', {'class': 'ZINbbc xpd O9g5cc uUPGi'})
	print('li')
	print(li)
	all_links = []
	for child in li:
		link = child.find('a', href=True)['href']
		all_links.append(link)
	#print(all_links)
	#print(len(all_links))
		
	description = soup.find_all(class_='BNeawe vvjwJb AP7Wnd')
	
	with open(category+'_news_'+str(page)+'.txt', 'w') as fp:
		for i in range(0,len(category_news)):
			news_title = category_news[i].get_text()
			news_description = description[i].get_text()
			news_link = all_links[i]
			
			fp.write(f'Title: {news_title}' + '\n')
			fp.write(f'Description: {news_description}' + '\n')
			fp.write(f'Link: {news_link}' + '\n\n')		
	fp.close()
	
if __name__ == '__main__':
	category = 'coronavirus'
	extract_news(category)
