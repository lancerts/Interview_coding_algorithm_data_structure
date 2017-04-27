f = open("knapsack_big.txt")
value=list()
weight=list()
totalw=2000000
totali=2000
m={}

for line in f:
    l=line.split()
    value.append(int(l[0]))
    weight.append(int(l[1]))

for i in range (0,totali+1):
    for j in range(0,totalw+1):
        m[i,j]=0
        
for  i in range (1,totali+1):
    for w in range (0,totalw+1):
        if weight[i-1]<=w:
            m[i,w]= max(m[i-1,w],value[i-1]+m[i-1,w-weight[i-1]])
        else:
            m[i,w]=m[i-1,w]
print m[totali,totalw]

