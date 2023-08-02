class student:
    def __init__(self , name):
        self.name = name 
        self.marks = []

        print(f"wicome {name} to the schoot ")

    def addMarks (self , marks):
        self.marks.append(marks)
    
    def avg (self):
        return sum(self.marks)/len(self.marks)
    

# s1 = student("hassan")
# print(s1.marks)
# s1.addMarks(60)
# s1.addMarks(55)
# s1.addMarks(50)
# s1.addMarks(70)
# print(s1.marks)


# print(s1.avg())


# class x:
#     def __init__(self , name):
#         self.name = name
#         self.marks=[]
#         print(f"hello {name} to maeks")
    
#     def add_maeks(self , marks):
#         self.marks.append(marks)

#     def avg (self):
#         return sum(self.marks)/len(self.marks)




# ha =x("hassan")

# ha.add_maeks(30)
# ha.add_maeks(20)
# ha.add_maeks(10)
# ha.add_maeks(50)
# print(ha.marks)

# print(ha.avg())


# class clk:
#     def __init__(self , a  , b):
#         self.a = a
#         self.b = b

#     def sun(self):
#         return self.a + self.b
    
#     def mull(self):
#         return self.a * self.b
        

# cln = clk(20 ,10)
# print(cln.sun())
# print(cln.mull())


# class con:
#     def __init__(self , a ,b):
#         self. a =a
#         self.b =b
#     def sum(self):
#         return self.a + self.b
#     def mull (self):
#         return self.a * self.b


# cc=con(20 , 40)
# print(cc.sum())
# print(cc.mull())

class cal :
    def __init__(self, a , b):
        self.a =a
        self.b =b
    
    def sum(self):
        return self.a + self.b
    def mull(self):
        return self.a * self.b
    
#   Inheritance عمليت توريث
# تم اخز النتاج نمن المثال السابك
class snms(cal):
    def add(self):
        return self.a ** self.b

x = snms(2 ,4)
print(x.add())
print(x.sum())
print(x.mull())