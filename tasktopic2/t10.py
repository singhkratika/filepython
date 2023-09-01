#wap to reverse digits of given no.
num=int(input("enterr a no reverse digits:"))
r=0
while num>0:
 remainder=num%10
 r=r*10+remainder
 num=num//10
print("REVERSE OF DIGITS = ",r)