#Write a python program to demonstrate super keyword.

class person:
    def _init_(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def fullname(self):
        print(firstname, ' ', lastname)
    
class student(person):
    def _init_(self, firstname, lastname, grade):
        self.grade = grade
        super()._init_(firstname, lastname) # calling base constructor
    def display_details():
        super().fullname() # calling base class method
        print('Grade ', self.grade)
        
std = student('James', 'Bond', '10')
std.display_details()