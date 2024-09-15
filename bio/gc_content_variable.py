#First Python Program
#Calculates GC Content

#Create a file handler
gene = open ('brca1.txt', 'r')

#set initial values
g = 0
c = 0
t = 0
a = 0

#skip the first line which is header
gene.readline()

for line in gene:
    line = line.lower()
    for ch in line:
        if ch == 'g':
            g +=1
        elif ch == 't':
            t += 1
        elif ch == 'c':
            c += 1
        elif ch == 'a':
            a += 1

print "Number of g's " + str(g)
print "Number of c's " + str(c)
print "Number of t's " + str(t)
print "Number of a's " + str(a)

gc = (g+c+.0) / (a + t + g + c)
print 'gc-content ' + str(gc)



