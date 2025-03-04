a=int(input("enter a value"))
b=int(input("enter b value"))
print("before swaping a is {} and b is {}".format(a,b))
temp=a
a=b
b=temp
print("after swaping a is {} and b is {}".format(a,b))

n=int(input("enter a number :"))
if n%2==0 :
        print("given number is even")
else:
        print("given number is odd")
print("end of program")

year =int(input("enter a year"))
if ((year%4==0 and year%100!=0)or year%400==0):
    print(year ,"is a leap year")
else:
    print(year,"is not a leap year")


a=int(input("enter 1st number:"))
b=int(input("enter 2 nd number:"))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a ")
print("end of program")
