#wap to create a list of ten nos by taking input from user.sum and average of nos.
l=[10,20,30,40,50,60,70,80,90,100]
print(type(l))
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])
print(l[6])
print(l[7])
print(l[8])
print(l[9])
sum=0
print("please enter the ten nos\n")
for i in range(1,11):
 num=int(input("number%d= "%i))
 sum=sum+num
avg=sum/10
print("the sum of 10 nos = ",sum)
print("the avg of 10 nos = ",avg)




