import csv 

with open('MP_Payment_Invoice_10000008175_20170307.csv', 'r') as howMuchMoolah:
    headerline = howMuchMoolah.next()
    total = 0
    disburse = 0
    commision = 0
    for row in csv.reader(howMuchMoolah):

    	total += float(row[6])
    	disburse += float(row[7])
    	commision += float(row[8])

    header = list(headerline.split(','))
    strSum = header[6]
    strDisburse = header[7]
    strCommision = header[8]

    print("%s: %s" % (strSum, total))
    print("%s: %s" % (strDisburse, disburse))
    print("%s: %s" % (strCommision, commision))
