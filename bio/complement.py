#Calculates Complement & Transcribe
import os
from string import maketrans
from collections import Counter

#Read FASTA file and skip its first line which is not part of data
gene = ''.join(open ( 'brca1.txt', 'r').readlines()[1:]).lower()

#show the first 50 of the data
print gene[:50]

#get complement of first 50
mapper = maketrans("actg", "ugac")
print gene[:50].translate(mapper)




