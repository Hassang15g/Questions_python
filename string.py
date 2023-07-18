
x  = "hassan"

print (x[0]) 
# النتج 
# h
print (x[0:3]) 
# النتج 
# has
print (x[0:]) 
# النتج 
# hassan

# format في طريقتاين لعمل 
# اولا طريقه
print ( "my name in %s and weight is %d kg !" %("hassan" , 23))
# # النتج 
# my name in hassan and weight is 23 kg !

# الثانيه
print ( "my name in {} and weight is {} kg !" . format("hassan" , 23))
# # النتج 
# my name in hassan and weight is 23 kg !


# الثلثه
x = "hassan"
print (f"my name in {x}  and weight is {23} kg !")
# النتج
# my name in hassan  and weight is 23 kg !




# Built-in String Methods
#  يعني اي فكشان موجوده في الغاي ممكان  استخدمه 
# مثال 

# capitalize()         تجعل اول الحروف كبيره
# Lower()                  تجعل  الحروف  صغيره
# Upper()                  تجعل  الحروف  كبيره
# isspace()                شوف لاو في مسافه 
# islower()                بشوف لاو هو حرف صغير 
# isupper()                بشوف لاو هو حرف كبير 
# count()       ("i")      بشوف الحرف المطلوب في نهايت الجمله 
# endswith()    ("hon")    بشوف الجمله  المطلوب في نهايت الجمله
# find ()                  بتعمل عمليت بحث ولو موجود بتحدد مكانه بي رقم الستر   
# index()                  بتعمل عمليت بحث ولو موجود بتحدد مكانه بي رقم الستر بس او مش موجوده بتعمل ارار
# replace()    ("in" , 'with')            بتعمل عمليت تبديل بين الكلمات الموجود والكلمه الي نا عمزه
# split()        (" ")           بيعمل عمليت فصل بين الكلم الموجود في الجمله  بي المسافه          

# center( 40 ,"0")                  بتستخدم بي عمليات التشفير بتكوم بملء الفرغات بين الحروف او الرقام لي نا بحدده مثال 40و"0 ده نا بقول الحروف او الرقام هي0 والمسافه هي 40
# مثال
s= "my name hassan"
print(s.center(40,"0"))
# النتيج
# 0000000000000 my name hassan 0000000000000











