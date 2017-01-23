import requests, pyperclip, re

ratEnterprisesString = requests.get('')
daGoodz = ratEnterprisesString.content # get raw content, minus encoding *ish

iPRegex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}') # IP Regex, could be shorter but c/would also be "moms spaghetti"
found = iPRegex.findall(daGoodz) # compare html string with regex.

print found[0] # debug/print first instance of matched regex
pyperclip.copy(found[0]) # copy IP Address string to clipboard.