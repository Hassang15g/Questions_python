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



