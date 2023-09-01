#wap to create a function named rev(),in rev()function pass a string and this function return reverse string.
def reverse(string):
 string = string[::-1]
 return string
s= "greeksforforgeeks"
print("the original string is:",end="")
print(s)
print("the reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))