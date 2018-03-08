import pyperclip, requests, time, csv

# Automatically sequentially name, and download video links.
# That are copied from browser 'inspect' feature, into the computer's clipboard

def dlFile(fileName, url):
	url = url.replace('\n', '').replace(' ', '')
	r = requests.get(url, stream=True)
	with open('Vid-%s.mp4' % fileName, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024): 
			if chunk:
				f.write(chunk)
	print fileName
	return fileName
	
def getLinksFromClipBoard(): #!!!This function needs to be manually broken. It is an endless while loop!!!
	MasterAry = []
	curClip = []
	x = 0

	while True:
		clipContents = str(pyperclip.paste())
		if clipContents not in curClip:
			curClip.append(clipContents)

			if [x, curClip[-1]] not in MasterAry and curClip[-1] != '':
				x += 1
				MasterAry.append([x, curClip[-1]])

				print MasterAry
				#dlFile(MasterAry[-1][0], MasterAry[-1][1])	
				with open('urls.csv', 'wb+') as cUrls:
					writer = csv.writer(cUrls)
					writer.writerows(MasterAry)
					time.sleep(1)

def dlVidsFromCsv(): # Once all links have been copied break above function. Run this function.
	with open('urls.csv', 'r+') as urls:
		reader = csv.reader(urls)
		for each in reader:
			dlFile(str(each[0]), str(each[1]))

#getLinksFromClipBoard()
#dlVidsFromCsv()
