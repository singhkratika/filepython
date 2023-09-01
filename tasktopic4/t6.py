#WAP TO FIND FACTORIAL OF GIVEN NUMBER USING RECURSION.
def fact(n):
 if n==0:
   return(1)
 else:
   return n*fact(n-1)
x=int(input("enter a nos to find of factorial: "))
print("factorial = ",fact(x))
