#wap in python to take a full name as input.now display short nmae of user.
name=input("enter name: ")
shortname=name.split(" ")
print("your name :",end=" ")
for n in range(len(shortname)-1):
  print(shortname[n][0]+".",end=" ")
print(shortname[len(shortname)-1]) 

