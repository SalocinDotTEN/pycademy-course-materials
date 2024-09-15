import os
import csv


data = [
    [1234, 'tom', 23, 'China'],
    [1234, 'tom', 23, 'China'],
    [1234, 'tom', 23, 'China']
]

csv.writer(open('mydata_noheader.csv', 'wb')).writerows(data)


data = [
    {'id':1234,
    'name':'tom',
    'age':23,
    'country':'China'},
    {'id':1235,
    'name':'Mac',
    'age':33,
    'country':'Malaysia'},
    {'id':1236,
    'name':'Jack',
    'age':43,
    'country':'India'}
]

f = open('mydata.csv', 'wb')
##writer = csv.DictWriter(f, data[0].keys())
writer = csv.DictWriter(f, ['id', 'name', 'age', 'country'])
writer.writeheader()
writer.writerows(data)
f.close()

reader = csv.DictReader(open('mydata.csv', 'rb'))
print list(reader)

reader = csv.DictReader(open('mydata_noheader.csv', 'rb'))
print list(reader)
