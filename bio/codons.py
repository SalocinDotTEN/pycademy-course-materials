#Extract Codons
import re
import os
from collections import Counter

#Create a file handler
gene = ''.join(open ( 'brca1.txt', 'r').readlines()[1:]).lower()

#Extract all codons and print the first 10 of them
codons = re.findall('...', gene)
print "First 10 codosn >> " + str(codons[:10])



