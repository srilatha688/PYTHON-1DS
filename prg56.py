n=int(input("enter a number:"))
sum=0
i=1
while(i<n):
    if(n%i==0):
       sum=sum+i
    i=i+1
if(sum==n):
        print(i,"is perfect")
else:
    print(i,"is not perfect")
    
       
