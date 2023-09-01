#Write a program in python to open a file for read operation. Also handle FileNotFoundErro

f=None
try:
 filename=input("Enter the filename to read : ")
 f=open(filename,"r")
 content=f.read()
 print(content)
except FileNotFoundError:
 print("The file doesn't exists")
finally:
 if f:
  f.close()
 print("File is closed")