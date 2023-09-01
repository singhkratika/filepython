#Write a program in python to take a decimal number as input and convert it into binary, octal and hexa-decimal equivalent.

# Python program to convert decimal number into binary, octal and hexadecimal number system
# Take decimal number from user
dec = int(input("Enter an integer: "))
print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")