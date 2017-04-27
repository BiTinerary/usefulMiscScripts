import smtplib, sys

subject = sys.argv[1]

lines = [line.rstrip('\n') for line in open('gmailCreds.txt', 'r')]

def emailCreds(subject):
  gmailAddress = lines[0] 
  gmailPass = lines[1]
  toMyPhone = lines[2]
  emailContent = """Subject: %s""" % subject #(subject.split(',')[0], subject.split(',')[1])

  return [gmailAddress, gmailPass, toMyPhone, emailContent] 

def sendEmail():
  gmailAddress, gmailPass, toMyPhone, emailContent = emailCreds(subject)

  try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmailAddress, gmailPass)
    server.sendmail(gmailAddress, toMyPhone, emailContent)
    server.close()
    print 'Email sent!'
    
  except:  
    print 'Something went wrong...'

sendEmail()