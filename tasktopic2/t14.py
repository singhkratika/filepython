#wap to print fibonacci series of prime numbers in given range.range must created by taking input from user.
n=int(input(" series is prime no "))
n1=0
n2=1
print("prime fibonacci series")
print(n1)
print(n2)
for i in range(1,n-1):
 n3=n1+n2
 print(n3)
 n1=n2
 n2=n3 