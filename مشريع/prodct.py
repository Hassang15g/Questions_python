# مثال يخد من المستخدم رقم ويشوف الرقم ده زوجي او فردي

while True :
    try :
        nunber =  input("enter bluth in number :")
        if nunber =="x":
            print("Thanks for the time")
            break
        nunber = int(nunber)
        if nunber % 2 == 0 :
            print("True")
        else:
            print("Folth")
    except ValueError:
        print("Please enter the correct number")
    
    print("-------------")










    