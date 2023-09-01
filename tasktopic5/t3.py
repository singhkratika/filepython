#wap to crate a class  with name reactangle class take two instance variables length and breadth.now create parameterrized constructor to initialize variable and create a method area9) which return area of reactangle .test the class reactangle.
class rectangle:
 def __init__(self,l,b):
   self.l=l
   self.b=b
 def rectarea(self):
   return(self.l*self.b)
x=int(input("enter the length: "))
y=int(input("enter the breadth: "))
r=rectangle(x,y)
print("area of reactangle:",r.rectarea())

  