'''
oop مفهيمك  
هام 4 مفهيم 
للشرح
1- Encapsulation
2- Polymorphism
3- Abstraction 
4- inheritance

'''
# و هو عبره عن نظام تغليف في بعد الخصاص  المفيده للكتابت الكود Encapsulation الاولن في حجه السم 
'''
طريكت Encapsulation الاول في 3 انوع من كتاب الكود بي 
class او 3 حلات من ظهور البينات في دخل 

1 - pudlic
مثال 
class my :
    def __init__(self, name):
        self.name= name            pudlic ده مده 
كده اقدر نا اشغله عدي 

one = my("hassan")
print(one.name)
وقد كمان اعدل عليه 
one.name = "hhhh"
pritn(one.name)

2 - Protected
هن لذم استخدم ال  _ قبل السم

مثال 
class my :
    def __init__(self, name):
        self._name= name            Protected ده مده 
كده اقدر نا اشغله عدي 

one = my("hassan")
print(one._name)

وقد كمان اعدل عليه 
one._name = "hhhh"
pritn(one.name)
        
3 - Private 
هن لذم استخدم 2 __ قبل السم
فقط classولذم تستخدم دخل ال 



'''


'''

Encapsulation شرح ما هو 
what is Encapsulation ?      هي المعن الحرفي ال التغليف

يحتويح البنات بدخله class يعني عبره عن 

مثال 
class nun {
    def sum (self , x ,y):
        self.x = x
        self.y = y
        return x + y
    
    def row (self , x ,y):
        self.x = x
        self.y = y
        return x * y
}

class كده نا بخد نسخه من ال 
"object"
s = nun()
s.sum(2 ,4)
s.row(2,4)
'''




