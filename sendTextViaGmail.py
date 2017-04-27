#Send SMS text to phone number. Ideally, run seperate script and based on results. Send text as notification of completion, change, etc...

import smtplib

subject = "Hellow There" #Subject text
content = "shtuff" #email body

lines = [line.rstrip('\n') for line in open('gmailCreds.txt', 'r')] # One liner, open gmailCreds.txt file.
# Each line corresponds to sensitive login data. Gmail address, password and phone number receiving the text. In that order.

def emailCreds(subject, content): # pass subject and body as arguments
	gmailAddress = lines[0] 
	gmailPass = lines[1]
	toMyPhone = lines[2]
	emailContent = """Subject: %s
%s""" % (subject, content) # Subject is internally recognized as command by gmail, newline indicates body text.

	return [gmailAddress, gmailPass, toMyPhone, emailContent] 

def sendEmail():
	gmailAddress, gmailPass, toMyPhone, emailContent = emailCreds(subject, content)
	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmailAddress, gmailPass)
		server.sendmail(gmailAddress, toMyPhone, emailContent)
		server.close()
    #^ necessary email/server settings ^
		print 'Email sent!'
    
	except:  
		print 'Something went wrong...'

sendEmail()
