
import time

f = open("knapsack1.txt")
value=list()
weight=list()
m={}

start = time.time()
for line in f:
    l=line.split()
    value.append(int(l[0]))
    weight.append(int(l[1]))

for i in range (0,101):
    for j in range(0,10001):
        m[i,j]=0
        
for  i in range (1,101):
    for w in range (0,10001):
        if weight[i-1]<=w:
            m[i,w]= max(m[i-1,w],value[i-1]+m[i-1,w-weight[i-1]])
        else:
            m[i,w]=m[i-1,w]
            
print m[100,10000]
print time.time() - start
