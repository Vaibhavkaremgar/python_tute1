#Student Class
# Create a Student class with:

# Attributes: name, roll_number, marks

# Method: display() that prints student info

# Method: is_passed() — returns True if marks > 40, else False

class Student():#Create a Student class
    def __init__(self,name,roll_number,marks):# Attributes: name, roll_number, marks
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):# Method: display() that prints student info
        print(f"{self.name} with {self.roll_number} roll_number got {self.marks} marks")

    def is_passed(self):# Method: is_passed() — returns True if marks > 40, else False
        if self.marks > 40:
            return True
        else:
            return False
Student1 = Student("Vaibhav",489,74)
Student1.display()
print(Student1.is_passed())
