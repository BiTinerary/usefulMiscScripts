import sys, csv

creader = csv.reader(open(sys.argv[1]))
cwriter = csv.writer(open(sys.argv[1].rstrip('.csv')+'NewGenerated.csv', 'wb'))


for cline in creader:
   new_line = [val for col, val in enumerate(cline) if col in (8,9,95,18,56,63,21,26,64,94,48,88,90)]#(8,9,18,21,26,48,56,63,64,88,90,94,95)]
   cwriter.writerow(new_line)