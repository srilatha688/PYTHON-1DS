def find_biggest(n1,n2):
    if(n1>n2):
      return n1
    else:
        return n2
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
print("the biggest number:",find_biggest(n1,n2))
