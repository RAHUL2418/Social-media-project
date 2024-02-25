import numpy as np
from collections import Counter
import csv
with open("E:\cit assignments\project\hashtags.csv", 'r') as file:
    reader = csv.reader(file)
    peoples = []
    for row in reader:
        peoples.append(row)
a=[]
for i in range(1,len(peoples)):
    a.append(peoples[i])
b=[]
for i in a:
    b=b+i
split_sentences = [sentence.split("#") for sentence in b]
c=[]
for t in split_sentences:
    c+=t
frequency = Counter(c)
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
h=[]
for e in range(2,12):
    h.append(sorted_frequency[e])
d=[]
for i in h:
    d.append(i[0])
print(d)
