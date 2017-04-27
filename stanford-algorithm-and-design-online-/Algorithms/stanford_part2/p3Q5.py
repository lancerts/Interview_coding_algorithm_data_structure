def p(i,j):
    sum=0;
    for k in range (i,j+1):
        sum=sum+a[k-1]
    return sum



m = {}
a=[0.2,0.05,0.17,0.1,0.2,0.03,0.25]
for i in range(1,8):
    for j in range (1,8):
        if j==i-1:
            m[i,j]=0
        elif j==i:
            m[i,j]=a[i-1]
        else:
            m[i,j]=0



for k in range (1,7):
    for i in range (1,8-k):
        j=i+k
        l=[]
        for r in range (i,j+1):
            if r==i:
                x=m[r+1,j]
            elif r==j:
                x=m[i,r-1]
            else:
                x=m[i,r-1]+m[r+1,j]
            l.append(x)

        m[i,j]= p(i,j)+min(l)
print m[1,7]





