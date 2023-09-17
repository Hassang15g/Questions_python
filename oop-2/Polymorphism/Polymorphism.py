'''
Polymorphism شرح  
المعني التعدد 
يعني امر ينفز الملر علي حسب المكان الذي في 
مثل 

كده نا عندي افكشاتن نفسه وكول فكشانى بتعمل حجه معينه  

class A :
    def do(self):
        print("form Class A")
        raise NotImplementedError(" Derived class must Implement this method")



class B( A ) :
    def do(self):
    print("form Class B")



class C ( A ) :
    def do(self):
    print("form Class C")



'''



