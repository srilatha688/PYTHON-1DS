def swap_by_value(n1,n2):
     temp=n1
     n1=n2
     n2=temp
     return n1,n2
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("before swap:a=",a,"and","b=",b)
a,b=swap_by_value(a,b)
print("after swap:a=",a,"and","b=",b)
