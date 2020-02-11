def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def multiply(x,y):
  return x*y
def devide(x,y):
  return x/y
print ("select operation,1=add,2=sub,3=multiply,4=devide")
choice=input("enter choice 1/2/3/4:")
num1=float(input("enter no.1="))
num2=float(input("enter no.2="))
if choice=="1":
  print(num1,"+",num2,"=",add(num1,num2))
elif choice=="2":
  print(num1,"-",num2,"=",sub(num1,num2))
elif choice=="3":
  print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="4":
  print(num1,"/",num2,"=",devide(num1,num2))
else:
 print("false choice")
