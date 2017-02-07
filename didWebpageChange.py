# Is webpage still down? Has a specific change been made to a page? Check every 15 seconds.
# Works only on basic sites that don't require browser headers, or block basic scrapers.
# ie: If a site offers an API, this will not work. Either incorporate Selenium IDE, their API, or CLI based browser
# to cross reference html source.

import re
import time
import requests

url = 'www.placeAUrlHere.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

daGoodz = requests.get(url, headers=headers)
contentz = daGoodz.content

def getUpdate():
	with open('tempTextFileOfHTMLSourceCode.txt', 'w') as overWriteFile:
	    overWriteFile.write(contentz)
	    overWriteFile.close()

def readFile():
	with open('tempTextFileOfHTMLSourceCode.txt', 'r') as readOnlyFile:
		findThis = "We're having technical difficulties and are looking into the problem now."
		lines = readOnlyFile.readlines()
		for line in lines:
			findMe = re.findall(str(findThis), line) # findThis string within this thing (line)
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
