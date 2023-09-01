#wap a program to find roots of quardatic equation ax^2+bx+c=0.
import math
def equationroots(a,b,c):
 dis=b*b-4*a*c
 sqrt_val= math.sqrt(abs(dis))
dis=int(input("discrimination no:"))
if dis > 0:
 b=int(input("no of quardetic equation"))
 a=int(input("no of quardetic equation"))
 print('real and different roots')
 print((-b+math.sqrt(dis))/(2*a))
 print((-b-math.sqrt(dis))/(2*a))
elif dis == 0:
 print('real and same roots')
 print(-b/(2*a))
else:
 print('complex roots')
 print(-b/(2*a),'+',sqrt_val,'i')
 print(-b/(2*a),'-',sqrt_val,'i')
a=1
b=10
c=-24
if a== 0:
   print('input correct quardatic equation')
else:
 equationroots(a,b,c)