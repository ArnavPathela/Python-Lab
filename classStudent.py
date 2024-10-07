class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

student1 = student("Bob",2432)
student2 = student("Sam",2433)

print(f"student 1 details: name - {student1.name} , rollno - {student1.rollno}")
print(f"student 2 details: name - {student2.name} , rollno - {student2.rollno}")
