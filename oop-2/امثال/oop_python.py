class Student :
    def __init__(self , name , age , cr):
        self.__name = name 
        self.age = age
        self.cr = cr
    
    def pop(self):
        print(f"my name is {self.__name} and age {self.age}")
# Encapsulation {
    def get_name(self):
        return self.__name
    def set_name(self , myNaem):
        self.__name= myNaem
        return myNaem
# }

    def com(self , num):
        if self.age <=num:
            print("Student not olp")
        else:
            print("Student and old")

Student_1 = Student("hassan" , 23 , "Amit")

# Encapsulation{
Student_1.set_name("hgghghgh")
# }
Student_1.pop()


# Student_1.com(20)
# print(Student_1.name ,Student_1.age , Student_1.cr)
# Student_1.name= "Ahmed"
# print(Student_1.name)





a =[ 1,2,3]
b = a.copy()

# print(a is b)


x = "Python coding"
y = False
z =(x [2:6] =="thon")

z= int (z)
print(z)