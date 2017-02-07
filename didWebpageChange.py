# Is webpage still down? Has a specific change been made to a page? Check every 15 seconds.
# Works only on basic sites that don't require browser headers, or block basic scrapers.
# ie: If a site offers an API, this will not work. Either incorporate Selenium IDE, their API, or CLI based browser
# to cross reference html source.

import re
import time
import requests

url = 'https://www.walmart.com/ip/Luminara-19-Heritage-Indoor-Outdoor-Lantern-Red-TEST/884755658'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

daGoodz = requests.get(url, headers=headers)
contentz = daGoodz.content

def getUpdate():
	with open('wallyDownText.txt', 'w') as wallyText:
	    wallyText.write(contentz)
	    wallyText.close()

def readFile():
	with open('wallyDownText.txt', 'r') as wallyTextTwo:
		findThis = "We're having technical difficulties and are looking into the problem now."
		lines = wallyTextTwo.readlines()
		for line in lines:
			findMe = re.findall(str(findThis), line)
			if findMe == []:
				continue
			elif findMe == ["We're having technical difficulties and are looking into the problem now."]:
				print findMe
				print "WE ARE STILL DOWN!!!"
			else:
				print "We Are Good Now"
				break

while True:
	getUpdate()
	readFile()
	time.sleep(15)
