#WAP TO CREATE A FUNCTION CALC(),WRITE CODE TO FIND SUMMATION,SUBTRATION ,MULTIFLICATIONAND DIVISIONAND RETURN IN FORM OF LIST.NOW TEST CALC()FUNCTION.
def calc(x,y):
 return[x+y,x-y,x*y,x//y]
x=int(input("enter first no : "))
y=int(input("enter second no : "))
print("SUM = ",x+y)
print("SUB = ",x-y)
print("MUL = ",x*y)
print("DIV = ",x//y)

 
