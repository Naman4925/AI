total=3000
load=1000
distance=1000
lose=0

start=total
for i in range(distance):
    while(start>0):
        start-=load
    if(start==1):
        lose-=1
    lose+=2
    lose-=1
    
    start=total-lose
    if(start==0):
        break

print(start)
