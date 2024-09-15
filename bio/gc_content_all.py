#Calculates GC Content
#create counter
from collections import Counter
c = Counter()

#Create a file handler
c.update(''.join(open ('brca1.txt', 'r').readlines()[1:]).lower())

gc = (c['g']+c['c']+.0) / (c['a'] + c['t'] + c['g'] + c['c'])

print 'gc-content ' + str(gc)






