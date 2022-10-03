import sys

i = []
b = []
t = 0
m = 0
k = 0
g = 0


for a in input().split():
    i.append( int(a) )
    t = t+1

for a in input().split():
    b.append( int(a) )
    m = m+1

d = t-m
if d < 0:
    print(0)
    sys.exit

for aa in range(d+1):
    for aaa in range(m):
        if i[aa+aaa] == b[aaa]:
            k = k+1
    if k == m:
        g = g+1
    
    k = 0

print(g)

