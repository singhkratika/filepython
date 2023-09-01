#wap in python to take a string as input.now check given string is palindrome or not.
str=input("enter string")
revstr="".join(reversed(str))
print("revstr")
if str==revstr:
 print("string is palindrome")
else:
 print("string is not palindrome")
  
