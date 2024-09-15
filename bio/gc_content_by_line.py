#First Python Program
#Calculates GC Content

#create counter
from collections import Counter
c = Counter()

#Create a file handler
gene = open ('brca1_BAP1.txt', 'r')

#Skip first line of FASTA data
gene.readline()

#Go through of FASTA lines
for line in gene:
    line = line.lower()
    #update last count of A, C, T, G from current line
    c.update(line)

gc = (c['g']+c['c']+.0) / (c['a'] + c['t'] + c['g'] + c['c'])
print 'gc-content ' + str(gc)



