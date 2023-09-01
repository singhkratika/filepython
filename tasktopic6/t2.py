#Write a python program to create a class named Shape. In Shape class create a method named setValue(), this method initialize side of shape. By inheriting Shape class create a new class Square. In Square class create a method area(), this method return area of square. Now by inheriting Shape class create a new class Cube. In Cube class create a method volume(), this method return volume of cube. Now Test Square and Cube classes.

class Shape:
 def setValue(self,s):
   self.s=s
class Square(Shape):
  def area(self):
   return self.s*self.s
class Cube(Shape):
 def volume(self):
  return self.s*self.s*self.s
x=int(input("Enter side of square : "))
sq=Square()
sq.setValue(x)
print("Area of square:",sq.area())
x=int(input("Enter side of cube : "))
cu=Cube()
cu.setValue(x)
print("Area of square:",cu.volume())