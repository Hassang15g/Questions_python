# مشروع للجدول الضراب 

# for x in range(1 , 13):
#     for y in range(1 , 13):
        
#         print( x, 'x' , y , '=' ,x*y)
#     print("-------------------------")
'''
النتاج هي جدول الضراب 
'''

con = int(input("Enter prise number : "))
nus = int(input("Enter, please use "))
for x in range(con , nus):
    for y in range(1 ,13):
        print(x , 'x' , y ,'=' , x*y)
    print("------------------------------")


