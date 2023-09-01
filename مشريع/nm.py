print("😃😆😂")
print("Welcome to my island ! ")
print("There are two doors in front of you. 🚪 a red door and 🚪 a blue door  ")
name = input("which door do you want to open? ")

if name == "blue" :
    print("Oops! You chose the crocodile door. \n Game Over! 🐊 🐊 🐊")
elif name == "red":
    print( """
Great! now you entered a room. 
    you found three boxes  🎁 white , 🎁 black , 🎁 green : 
""" )
    con = input("which box do you open ? :")
    if con =="white":
        print("oops! You opened a box filled with snakes🐉🐉🐉")
    

