import sys, csv
onlyTheseHeaders =  ["Auth Units", "Canceled Units", "Gross Units", "Authorized Sales", "Canceled Sales", "GMV", "Commission Charged"]

def inputFile(filename, addAllTheseNumbers):
	with open(str(filename), 'r+') as csvFile:
		reader = csv.DictReader(csvFile)
		columnTotal = 0

		for line in reader:
			columnTotal += float(line[addAllTheseNumbers])
		csvFile.close()
	prettyPrint = ("%s: %s" % (addAllTheseNumbers, columnTotal))
	return prettyPrint

def loopEachHeader(csvFile):
	for each in onlyTheseHeaders:
		finalGoods = inputFile(csvFile, each)
		with open('outputLog.txt', 'a+') as output:
			output.write(finalGoods + '\n')
		print finalGoods
loopEachHeader(sys.argv[1])

# Run from CLI with input file as first argument. ie: python thisScriptName.py inputFile.csv
# input file should be .csv with header
# Script will add numerical values of each column, not including the header.
# Then print/output "Header Name: Sum of Column"
# 
# input .csv should look like this:
#
# header, contents, goHere, andHere, andHereToo
# 1, 2, 3, 4, 5
# 1, 2, 3, 4, 5
# 1, 2, 3, 4, 5
#
# output will look like this:
#
# Header: 3
# Contents: 6
# goHere: 9
# andHere: 12
# andHereToo: 15