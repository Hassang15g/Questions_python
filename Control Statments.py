# ######################################
# Control 
        #   loops الدوات التحكم في الشوط او 
# 1 - Break 
# 2 - Continue
# 3 - Pass


# for i in "python":
#     if i == "h":
#         break
#     print("Current i " ,i)

# (h) النتج يتم تشغيل لبرنمج لحد ) 
# Current i  p
# Current i  y
# Current i  t


# x = 10 
# while x > 0 :
#     # print (" current ", x)
#     x -=1
#     if x == 5:
#         break
#     print("current" ,x)

# Questions

# print("Number    Square")
# print("-----------------")
# for i in range (1,11):
#     square = i * i
#     print(i , "\t", square )

# النتج
# Number    Square
# -----------------
# 1        1
# 2        4
# 3        9
# 4        16
# 5        25
# 6        36
# 7        49
# 8        64
# 9        81
# 10       100

# \n   new line         خط جديد 
# \t   tab = 4 spaces    علامة التبويب = 4 مسافات

# print ("Number \t Square")
# print ("----------------------")
# for i in range(1 , 11):
#         square = i ** i
#         print ( i , "\t" , square)
# النتج
# Number   Square
# ----------------------
# 1        1
# 2        4
# 3        27
# 4        256
# 5        3125
# 6        46656
# 7        823543
# 8        16777216
# 9        387420489
# 10       10000000000

# ده معتمد علي الرقم المفرود ان يتم 
# المستخدم ان يدخله وبعدين اعمل العمليه الطرب

# start = input("Enter the start Number :")
# age = input("How Should  I Go :")

# for i in range(int(start), int(age)+1):
#         Square = i*i
#         print( i , Square)

# النتج
# Enter the start Number :5
# How Should  I Go :10
# 5   25
# 6   36
# 7   49
# 8   64
# 9   81
# 10  100

# *************************************************
#  * فكرت النجوم 

# rows = int(input("How Many Rows : "))
# cols = int(input("How Many Cols : "))

# for r in range(rows):
#         for c in range(cols):
#                 print("*" , end="")
#         print()
# النتج
# **********
# **********
# **********
# **********
# **********

#  فكرت  الهرام بي النجوم

# for r in range(10):
#         for c in range(r+1 ):
#                 print("*" , end="")
#         print()
# النتج
#     *
#     **
#     ***
#     ****
#     *****
#     ******
#     *******
#     ********
#     **********


# x = ["fgf" , "g", 44]
# for i in x :
#         print(i)

# lists = [[1, 3 , 4] , [5 , 6 ,7] , [8 ,9 , 10]]
# for i in lists :
#         print(i)
#         for c in i :
#                 print(c)
        

