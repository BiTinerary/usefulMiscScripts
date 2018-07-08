import requests, pyperclip
from bs4 import BeautifulSoup

url = 'https://icanhazdadjoke.com/'

def getDadJoke(url):
	get = requests.get(url).content
	soup = BeautifulSoup(get, 'html.parser')
	joke = soup.find_all('p', class_='subtitle')[0].text#attrs={'class': 'subtitle'})#, class_="subtitle")[0]

	print joke
	return str(joke)

pyperclip.copy(getDadJoke(url))