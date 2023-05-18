n=int(input("Enter the number:")) 
if n%2==0: 
    for i in range(1,n+1): 
        t=((2*i)-1) 
        for j in range(1,t+1): 
            if j==1: 
             print((' '*(n-i)),j,end='') 
            else: 
             print(j,end='') 
        print() 
