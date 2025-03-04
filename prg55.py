n=int(input("enter a number:"))
sum=0
num_digit=len(str(n))
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**num_digit
    temp//=10
if n==sum:
        print(n,"is a armstrong number")
else:
            print(n,"is not a armstrong number")
