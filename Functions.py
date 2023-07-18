########################################################
########### Functions
# function Arguments شرح انوع ال 
# '''
# 1-Required arguments            الوسيطات المطلوبة
# 2-Keyword arguments             وسيطات الكلمات الرئيسية
# 3-Default arguments             الوسيطات الافتراضية
# 4-Variable-length arguments     وسيطات متغيرة الطول    
# '''


'''
عمل فكشان للجمع عددين 

1-Required arguments

def sun (x , y ):
    print (x + y)
    return

sun(3 ,3)
sun (5 ,6)

النتج
6
11

'''
# ###################################

# 2-Keyword arguments             وسيطات الكلمات الرئيسية
# اهم حجه الترتيب في الفكشن

# def co (x , y):
#     print(x + y)

# co(y=5 , x=4)


# #######################
# 3-Default arguments             الوسيطات الافتراضية
# '''
# def sun (name , age = 20):
#     print (name  , age)
    


# sun ("hassn" , 3)
# sun ("hassan" )

# النتيج
# hassn 3
# hassan 20
# '''

# ##########################################
# 4-Variable-length arguments     وسيطات متغيرة الطول    

# vartuple          ←←←← للعمل جمع مع العناصر ممكانت عدده

# '''
# def myprint (arg , *vartuple):

#     result = arg
#     for i in vartuple :
#         result= result + i
#         print(result)

# myprint(10 , 3,4)

# # النتج
# 13
# 17
# '''

# Anonymous Functions
# هي تريقه للكتابت الفكشان  
# Anonymous اهم حجه للتعريف 
# لكي يتم فيه تخزين الفكشان lambda  هي 

# sun = lambda x ,y : x+y
# print(sun (1,3))
# النتج
# 4

# def x(age1 ,age2):
#     sun =age1 + age2
#     return sun


# print(x(5,5))