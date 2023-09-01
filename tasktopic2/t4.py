#wap to take coordinates of a point as input and determine its quadrant
x=int(input("enter the x-coordinate:"))
y=int(input("enter the y-coordinate:"))
if x<0 and y>0:
 print("the point is in the first quadrant")
elif x<0 and y<0:
 print("the point is in the second quadrant")
elif x<0 and y<0:
 print("the point is in the third quadrant")
elif x>0 and y<0:
 print("the point is in the fourth quadrant")
elif x== 0 and y== 0:
 print("the point is at the origin")
else:
 print("the point is on one of the axes")