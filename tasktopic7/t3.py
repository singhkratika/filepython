#Write a program in python to find division of two numbers. Also handle ValueError and ZeroDivisionError in same program.
def div(x,y):
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    result = numerator / denominator

except ValueError:
    print("Error: Please enter valid numerical values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Result of the division:", result)
try:
    # Prompt the user for the file name
    file_name = input("Enter the name of the file to open: ")

    # Attempt to open the file for reading
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")