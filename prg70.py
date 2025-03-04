import sys
n=len(sys.argv)
print('\n total number of arguments passed from command are:',n)
print('command line arguments passed are:',end=' ')
for i in sys.argv:
    print(i,end=' ')
sum=0
for i in range(1,n):
    sum=sum+int(sys.argv(i))
print('\n sum of numbers passed are:',end=' ')
for i in sys.argv:
    print(i,end=' ')
sum=0
for i in range(1,n):
    sum=sum+int(sys.argv(i))
print('\n sum of numbers passed as argument is:',sum)
