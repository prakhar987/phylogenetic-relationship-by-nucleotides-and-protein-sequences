#!/usr/bin/python
import csv
import re
source = open("Nucleotide.txt", "r")
matrix = [[], [], [], [], [], []]
name=[0,0,0,0,0,0]
length=0.0

for x in range(6): 
	line = source.readline()
	start = line.find('(') + 1
	end =   line.find(')', start)
	name[x]=line[start:end]
	# print name
	while True:
		c = source.read(1)
		if c == '>' or c=='':
			break
		if (c!='\n' and c!='\r') :
			matrix[x].append(c)
			if x==0:
				length+=1

distance = [[0 for x in range(6)] for x in range(6)]

x=0
for x in range(6):
	for y in range(x+1,6):
		mismatch=0
		for z in range(int(length)):
			if(matrix[x][z]!=matrix[y][z]):
				mismatch+=1
		distance[x][y]=mismatch/length
		distance[y][x]=mismatch/length
		

# formatting
for x in range (6):
	a=[0]
	a[0]=name[x]+'     '
	distance[x]=a+       distance[x]

Poutput = open("Ndistance.txt", "w")
print>>Poutput,"*     ,",
for x in range(6):
	print>>Poutput,name[x], '     ,',
print>>Poutput,''



writer = csv.writer(Poutput)
for i in range(len(distance)):
	writer.writerow(distance[i])
Poutput.close()

