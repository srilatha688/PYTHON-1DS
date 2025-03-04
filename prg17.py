def add(x,y):
    return x+y
def  subrat(x,y):
    return x-y
def divied(x,y):
    return multiply
print("select opertion number from be low menu:")
print("1.add ")
print("2.subrat")
print("3.divied")
print("4.multiply")
choice =input("enter first number:")
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
if   choice =='1':
           print(num1,"+",num2,"=",add(num1,num2))
elif  choice=='2':
          print(num1,'-',num2,'=',subtrat(num1,num2))
elif   choice=='3':
          print(num1,'/',num2,'=',divied(num1,num2))
elif  choice=='4':
         print(num1,'*',num2,'=',multiply(num1,num2))
else :
         print('invalid choice') 

