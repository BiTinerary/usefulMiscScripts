import requests, json

getImagesForWebsites = ['www.google.com', 'www.walmart.com', 'www.stackoverflow.com', 'www.github.com', 'www.symbaloo.com']

#goGetImageJson = requests.get('https://icons.better-idea.org/allicons.json?url=https://walmart.com')

for each in getImagesForWebsites:
	goGetImageJson = requests.get('https://icons.better-idea.org/allicons.json?url=https://%s' % each)
	jString = goGetImageJson.content
	jLoads = json.loads(jString)

	print(jLoads['icons'][0]['url'])
