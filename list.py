# list ??
list1 = ["my python" , True , 1234]

# Accessing values in List    الوصول إلى القيم في القائمة

list2 = ["my python" , True , 1234]
print(list2[0] )
# النتيج
# my python
print(list2[1] )
# النتيج
# True

# Updating list       list العدل في 
# مثال
list3 = ["python " ,22222 , True , False]
list3[1]= 33333;
print(list3)


# delete List       لحزف العنصر 
# مثال 

list_1= ["python " ,22222 , True , False]
del list_1[1]
print(list_1)
# النتج بعد الحزف
# ['python ', True, False]

'''
Built-in String Methods

len()             وعداد العناصر الموجوده list بجيب طول ال  \

pop()               list بتعمل عمليت ضبعه ثم تكوم بي حزفه من ال                   

reverse()         يعني الاول يبق في الخر والعكس صحيح list نبعمل  عمل تبديل ماكان العناصر داخل ال 

count()           بشوف في كلمات ممكراره ولو في بيجيبه 

append()          list  ولكن في اخر ال  listبتعمل اضفه في ال 

insert()          مع تحديد المكان الذي اريده list بتعمل اضفه في ال 
'''

# مثال
list_2= ["python " ,22222 , True , False]

list_2 .insert(1 ,"math")
print(list_2)

# النتج
# ['python ', 'math', 22222, True, False]

# delete List 
# مثال 

delets = ["python" , 12344 , True , False]

del delets[2]
print(delets)
# النتج بعد الحزف 
# ['python', 12344, False]

# pop() مثال علي  
pops = ["python" , 12344 , True , False]
pops.pop()
print (pops)
# النتج 
# ['python', 12344, True]

#reverse() مثال عن      
list_3= ["python" , 12344 , True , False]

list_3.reverse()
print(list_3)
# النتج
# [False, True, 12344, 'python']

