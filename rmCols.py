import sys, csv

reader = csv.reader(open(sys.argv[1]))
writer = csv.writer(open(sys.argv[1].rstrip('.csv')+'-Slim.csv', 'wb'))

x = 0

for line in reader:
   newLine = [value for column, value in enumerate(line) if column in (8,9,95,18,56,63,21,26,64,94,48,88,90)]#(8,9,18,21,26,48,56,63,64,88,90,94,95)]
   writer.writerow(newLine)
   print x
   x += 1
writer.writerow(str(""",=sum(B2:B%s),,,=sum(E2:E%s),=sum(F2:F%s),,,=sum(I2:I%s),,,=sum(L2:L%s),,""" % (x,x,x,x,x)).split(','))
