#wap to find sum digits of given no.
num=int(input("enterr a no sum digits:"))
sum=0
while num>0:
 remainder=num%10
 sum=sum+remainder
 num=num//10
print("SUM OF DIGITS = ",sum)