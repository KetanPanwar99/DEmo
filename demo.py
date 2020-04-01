#code
t=int(input())
for _ in range(t):
    m,n=list(map(int,input().split()))
    a=list(map(int,input().split()))
    mat=[]
    c=0
    temp=[]
    for i in a:
        if c==n:
            mat.append(temp)
            temp=[i]
            c=1
        else:
            temp.append(i)
            c+=1
    mat.append(temp)
    print(mat)
    
    for i in range(m):
        print(mat[i])
    res=0
    i=0
    r=0
    while i<n and r<m:
        while i<n-1 and mat[r][n-i-1]==1:            
            i+=1
            print(r,i,n,mat[r][n-i-1])
        r+=1
        if r<m and i<n and mat[r][n-i-1]==1:
            res=r
            i+=1
        
    #print(r,i,n,mat[r][n-i-1])     
    print(res)
          
            
        
        
