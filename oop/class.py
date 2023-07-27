'''
classشرح ال 
تنقصم ال 2 حجات 
مهام 
porperties
methods

class وهم بختصار تتكوين اي 
porpertiesيعني ان
اب حجه ثبته لاتتلب اي اكشان 
مثال
color

او حجه لا فيه اي اكشان او حرقه


ام 
methods هي بختصار اي حجه فيه حرقه 
devده  يستخدام في  
مثال
'''
class cods():
# porperties
    color = "red"
# methods = functions
    def open_door (self):
        print("open_door")

    def close_door(self):
        print("close_door")    



# x = cods()
# x.open_door()
# x.close_door()


'''
selfلذم استخدام  
مع الي فكشان للحجز مكان المتغير      
مثال

'''

# class myTset():
#     def text(self):
#         print(self)
#         print("hghghghghgh")

# x = myTset()
# x.text()
class student:
    def st_student(self , name , age):
        self.name = name
        self.age =age
        print(f"I am {name} is and age {age}")

su = student()
su.st_student("" , 23)
# النتج
# I am  is and age 23

'''
constructor :
methodهو عبر عن 
constructorمن الكلس يتم تنفيز ال objectيتم تنفيزه  الاول ما تخد 
مثال
'''

class up :
    def __init__(self , name , age):
        self.name =name
        self.age = age
        print(f"I am is {name} is age {23}")

su = up('hassan', 23)
# النتيج
# I am is hassan is age 23
'''
objectيتم تنفيز الفكشان اول ما اخد منه 
يتم تنفيزه  
__inti__ ولكن لذم يكون السم الفكشان 

'''

