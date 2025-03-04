def calc(a,b):
   c=a+b
   d=a-b
   e=a*b
   f=a/b
   g=a//b
   h=a%b
   i=a**b
   return c,d,e,f,g,h,i
results=calc(2,3)
print("multiple values returned are",results)
t,u,v,w,x,y,z=calc(2,3)
print("sum=",t)
print("difference=",u)
print("product=",v)
print("division=",w)
print("floor division=",x)
print("modulus=",y)
print("power=",z)

