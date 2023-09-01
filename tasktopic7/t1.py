#Write a program in python to create a class with name Figure. In Figure class create a single method named area(), by using area() method find area of square and rectangle as an example of method o

class Figure:
    def area(self, *args):
        if len(args) == 1:
            # Calculate the area of a square (side * side)
            side = args[0]
            return side * side
        elif len(args) == 2:
            # Calculate the area of a rectangle (length * width)
            length, width = args[0], args[1]
            return length * width
        else:
            return "Invalid number of arguments"

# Create an instance of the Figure class
figure = Figure()

# Calculate the area of a square
square_area = figure.area(5)
print("Area of the square:", square_area)

# Calculate the area of a rectangle
rectangle_area = figure.area(4, 6)
print("Area of the rectangle:", rectangle_area)

# Try to calculate with an invalid number of arguments
invalid_area = figure.area(3, 7, 2)
print(invalid_area)

