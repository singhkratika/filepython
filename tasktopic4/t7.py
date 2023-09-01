#WAP TO GENERATE FIBONACI SERIES UP TO N TERM USING RECURSION.
def fab(n):
 if n==0:
 return(1)
n=int(input(" fibonacci series : "))
n1=0
n2=1
print(n1)
print(n2)
else:
   return n*fab(n-1)
x=int(input("enter a nos to find of fabonacci: "))
print("fabonacci = ",fab(x))

for i in range(1,n-1):
 n3=n1+n2
 print(n3)
 n1=n2
 n2=n3 
