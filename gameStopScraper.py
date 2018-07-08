import requests
from bs4 import BeautifulSoup

def gamestopScraper(url):

	get = requests.get(url)
	data = get.content
	soup = BeautifulSoup(data, 'html.parser')

	image = soup.find_all('div', class_='fluidItem itemPicture ats-trade-quote-itempic')[0]
	imgCode = image.find_all('img')[0]['src']

	gameTitle = soup.find_all('div', class_='title ats-trade-quote-item-title')[0]
	regularPricing = soup.find_all('div', class_='basicBox')[0]
	cashVal = regularPricing.find_all('div', class_='regularPrice ats-trade-quote-tradevalue-regprice')[0]
	dolla, cashText = cashVal.find_all('span', class_='priceAmount')[0], cashVal.find_all('div', class_='valueText')[0]

	title = gameTitle.get_text()
	imgLink = 'https://www.gamestop.com%s' % imgCode
	valueInfo = [cashText.get_text(), dolla.get_text()]

	return [title, valueInfo, url, imgLink]

def webpageExists(url):
	get = requests.get(url)

	if get.status_code == 404:
		print get.status_code
		pass
	else:
		return gamestopScraper(url)

with open('games.html', 'a+') as games:
	for each in xrange(100000):
		print each

		try:
			title, valueInfo, url, imgLink = webpageExists('https://www.gamestop.com/trade/quote/ps3/%s' % each)
			games.write('<br><a href="%s"><img src="%s"></a><br>%s<br>%s: %s' % (url, imgLink, title, valueInfo[0], valueInfo[1]))
			print 'success'

		except Exception as e:
			print e, 'fail'