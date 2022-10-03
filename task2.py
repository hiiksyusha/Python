import sys

N = int(input())
k = int(input())
a = []
p=0;
indict = []

for i in input().split():
    a.append(int(i))

kol = max(a)
    
for i in range(kol):
    indict.append(0)
    
for i in range(k):
    if i % 2 == 0:
        for ii in range(a[i],a[i+1]):
            indict[ii] = 1
            
    
for f in range(N-1):
    
    kk = int(input())
    if kk == 0:
        p =1;
        break;
    aa = []
    for ii in input().split():
        aa.append(int(ii))
    
    
    for i in range(kk):    
        if aa[i] > kol:
            aa[i] = kol
    
        
    
    for i in range(aa[0]):
        indict[i] = 0
    
    if aa[-1] < kol:
        for i in range(aa[-1],kol):
            indict[i] = 0
        
    
    for i in range(kk-1):
        if i % 2 == 1:
            for ii in range(aa[i],aa[i+1]):
                if ii < kol:
                    indict[ii] = 0
                    

    
outt =[]
if indict[0] == 1:
    outt[0] == 0
    
for f in range(1,kol-1):
    if indict[f] == 1 and indict[f-1] == 0 and indict[f+1] == 1:
        outt.append(f) 
    if indict[f] == 1 and indict[f-1] == 1 and indict[f+1] == 0:
        outt.append(f+1) 
    if indict[f] == 1 and indict[f-1] == 0 and indict[f+1] == 0:
        outt.append(f)
        outt.append(f+1)

if indict[-1] == 1 and indict[-2] == 0:
    outt.append(kol-1)

if indict[-1] == 1:
    outt.append(kol)
if p == 1:
    print(0)
else:
    h = len(outt)
    print(h)
    for i in outt: print(i, end = " ")