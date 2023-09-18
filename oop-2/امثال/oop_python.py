class Student :
    def __init__(self , name , age , cr):
        self.name = name 
        self.age = age
        self.cr = cr
    
    def pop(self):
        print(f"my name is {self.name} and age {self.age}")


Student_1 = Student("hassan" , 23 , "Amit")
print(Student_1.name ,Student_1.age , Student_1.cr)

# Student_1.name= "Ahmed"
# print(Student_1.name)

Student_1.pop()


