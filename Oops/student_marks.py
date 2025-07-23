#Student Class
# Create a Student class with:

# Attributes: name, roll_number, marks

# Method: display() that prints student info

# Method: is_passed() — returns True if marks > 40, else False


import math
class Student():#Create a Student class
    def __init__(self,name,roll_number,subject_marks):# Attributes: name, roll_number, marks
        self.name = name
        self.roll_number = roll_number
        self.subject_marks = subject_marks

    def display(self):# Method: display() that prints student info
        print(f"{self.name} with {self.roll_number} roll_number got {self.subject_marks} marks")

    def total_marks(self):
        return sum(self.subject_marks.values())
    def percentage(self):
        return self.total_marks()/len(self.subject_marks)

    def is_passed(self):# Method: is_passed() — returns True if marks > 40, else False
        return all(mark >=40 for mark in self.subject_marks.values())
    def grade(self):
        percent = self.percentage()
        if percent >= 85:
            return "A Grade"
        elif percent>=70:
            return "B Grade"
        elif percent>=55:
            return "C Grade"
        elif percent>=40:
            return "D Grade"
        else:
            return "Fail"
    def remarks(self):
        if self.is_passed():
            if self.grade() in ["A Grade", "B Grade"]:
                return("Excellent Work Keep It Up Champ!!")
            elif self.grade()== "C Grade":
                return("good work, need more from you")
            else:
                return("you need to visit tution for improvement")
        else:
            return("failed you idiot")

Students =[Student("Vaibhav",489,{"Math": 88, "Science": 76, "English": 91}),
           Student("akshay",490,{"Math": 45, "Science": 89, "English": 67}),
           Student("suraj",491,{"Math": 78, "Science": 71, "English": 94}),
           Student("bunty",492,{"Math": 65, "Science": 46, "English": 78}),
           Student("Chimtu",493,{"Math": 30, "Science": 30, "English": 39})
                   ]
for s in Students:
    ranked_students = sorted(Students, key=lambda s: s.percentage(), reverse=True)

print("\n" + "="*40)
print("🏆 RANKED STUDENT REPORT CARDS")
print("="*40)

for rank, s in enumerate(ranked_students, start=1):
    print(f"\n🎖️ Rank {rank}")
    print("-" * 30)
    s.display()
    print("The total marks are :-", s.total_marks())
    print(f"The percentage of the student is :- {s.percentage():.2f} %")
    if s.is_passed():
        print("Result:- Passed")
    else:
        print("Result:- Failed")
    print("Grade :-", s.grade())
    print(f"Remarks: -", s.remarks())
    print("_" * 30)
print("congrats!! All the top rankers", "-"* 30)
print("🏅 Final Ranking Order:")
for rank, student in enumerate(ranked_students[:4], start=1):
    print(f"Rank {rank}: {student.name}")
