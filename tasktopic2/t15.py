#wap to check given no is armstrong or not.
i=int(input("enter the input no:"))
n=i
sum=0
while n>0:
 rem=n%10
 sum=sum+rem*rem*rem
 n=n//10
if i==sum:
 print("this armstrong no:")
else:
 print("this is not armstrong no:")
