
import numpy as np
import csv
 
 
with open(r"C:\Users\ragul\Downloads\project\instagram_reach (1).csv", ) as file:
    reader = csv.reader(file)
    
    
    peoples = []
    for row in reader:
        peoples.append(row)
people=[]
u=[]
for i in peoples:
    u.append(i[0])
    u.append(int(i[1]))
    people.append(u)
    u=[]
for i in range(1, len(people)):
    j = i
    while j > 0 and people[j-1][1] > people[j][1]:
        people[j-1], people[j] = people[j], people[j-1]
        j -= 1

a=[]
for i in range(2,12):
    a.append(people[-i])
print(a)
