# مثال للعمل جمع عداد الذي يدخله المستخدام من الرقام


print ("this game will Take several numbers and print the average of them ?")

count_1 = int(input("how many Number would you like to sum  : ")) 

count_2 = 0
summ = 0
while count_2 < count_1 :
    nunn = float(input("Please use Pinter pl : "))
    summ += nunn
    count_2 +=1
    x = summ / count_1
print("Sum as",summ)
print("Average s." , x) 