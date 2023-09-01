# binary to decimal
binary=input("enter a binary no:")
decimal=0
power=0
for digit in binary[::-1]:
 if digit=='1':
   decimal+= 2**power
   power +=1
print("decimal equivalent :"",decimal)