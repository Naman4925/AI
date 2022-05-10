def TowerOfHanoi(n,source,dest,helper):
    if n==1:
        print("Move disk 1 from source to", source," destination",dest)
        return
    
    TowerOfHanoi(n-1,source,helper,dest)
    print("Move disk",n," from source to", source," destination",dest)
    TowerOfHanoi(n-1,helper,dest,source)

n=3
TowerOfHanoi(n,"A","B","C")
