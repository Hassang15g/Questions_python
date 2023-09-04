'''
python Tasks 
    simple code to print the multiplication table 
    like this :
        1 * 1 = 1
        1 * 2 = 2
    from 1 to 12 


'''
# i = int(input("Blaze enter again ?" ))
# z= int(input("Blaze enter again...... ?" ))

# for x in range(i , z+1) :
#     for y in range (1 ,13):
#         print(x ,'*', y , '=' , x*y)
#     print("_________________")





'''
عمل برنمج يضبع ارقم عشويه 
Random بي نستخدم مكتبه 

Randint يجب استخدام  Random للستخدم المكتبه 
لكي يستقبل رقم الاول و الرقم الثانى 
'''
# import random

# my_random = random.randint(0,10)
# print(my_random)


# random.seed(10)
# print(random.random()

while True :
    my_to = input("Please enter :")
    if my_to =="x":
        break
    my_go= input("Play Santor :")
    if my_go == "x":
        break

    if int(my_to ) < int(my_go) :
        for x in range( int(my_to ) , int(my_go)+1) :
            print(x)
