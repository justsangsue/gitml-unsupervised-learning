'''
Convert csv file to arff file for Weka
'''

#!/usr/bin/python
__author__ = 'tonsquemike'
import sys, getopt
import csv, sys, os

# Store input and output file names
ifile=''
ofile=''

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"i:o:")

###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-i':
        ifile=a
    elif o == '-o':
        ofile=a
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])

fileIn = open(ifile);
fileOut = open(ofile,"w")

lastPos = fileIn.tell()

fileOut.write("@RELATION CSC722Assignment3\n\n\n")
count=1

for k in range(len(fileIn.readline().strip().split(','))-1):
	fileOut.write("@ATTRIBUTE f"+str(count)+" numeric\n")
	count+=1

tempClass = []
for line in fileIn:
	tempClass.append(line.strip().split(',')[0]);
fileOut.write("@ATTRIBUTE outputClass {"+','.join(tempClass)+" }\n\n\n")

fileOut.write("@DATA \n");

fileIn.seek(lastPos)

tempStr = []
for line in fileIn:
	for i in range(len(line.strip().split(','))):
		if i!=0:
			tempStr.append(line.strip().split(',')[i])
		if i == len(line.strip().split(','))-1:
			tempStr.append(line.strip().split(',')[0])
			print tempStr
		i=i+1
	fileOut.write(','.join(tempStr)+"\n")
	tempStr= []


fileOut.close()
