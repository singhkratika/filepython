#wap to create a set of ten nos by taking input from user.now using traverse of set. 

list=[]
for i in range(10):
 num=int(input("enter the no: "))
 list.append(num)
print(list)
#traverse and print set of element
print("set element")
for num in list:
 print(num)