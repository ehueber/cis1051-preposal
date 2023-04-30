### Title : The ultimate password generator 
### Name: Ellen Hueber, senior  Matt Sivo, junior

import turtle
import random

bob = turtle.Turtle()
bob.speed(15)
bob.width(1)

bob.up()
bob.goto(-150,50)
bob.down()

bob.fillcolor("red")
bob.begin_fill()
bob.right(180)
bob.circle(50,180)
bob.forward(50)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(50)
bob.end_fill()

bob.up()
bob.right(180)
bob.forward(50)
bob.down()

bob.fillcolor("orange")
bob.begin_fill()
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.end_fill()

bob.up()
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.down()

bob.fillcolor("yellow")
bob.begin_fill()
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.end_fill()

bob.up()
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.left(270)
bob.down()

bob.fillcolor("green")
bob.begin_fill()
bob.right(180)
bob.forward(50)
bob.circle(50,180)
bob.forward(50)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(50)
bob.end_fill()

bob.up()
bob.left(180)
bob.forward(50)
bob.right(90)
bob.forward(100)
bob.left(90)
bob.down()

l, c, n, s = 0, 0, 0, 0
password = input("enter password:")

capital=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

lower=("abcdefghijklmnopqrstuvwxyz")

special=("$@_!&#*?:;\|%^")

number=("0123456789")
for i in password:
    if (i in lower):
        l+=1           
    if (i in capital):
        c+=1           
    if (i in number):
        n+=1           
    if(i in special):
        s+=1       
if (l>=1 and c>=1 and n>=1 and s>=1 and len(password)>12):
    print("password is great")
    
    #for green
    bob.right(180)
    bob.forward(25)
    bob.left(180)
    bob.fillcolor("black")
    bob.begin_fill()
    bob.right(60)
    bob.forward(50)
    bob.right(120)
    bob.forward(50)
    bob.right(120)
    bob.forward(40)
    bob.end_fill()
    bob.up()
    bob.goto(100,110)
    bob.down()

elif (l>=1 and c>=1 and n>=1 and s<1 and len(password)>8):
    print("password is good")
    #for yellow
    bob.forward(50)
    bob.fillcolor("black")
    bob.begin_fill()
    bob.right(60)
    bob.forward(50)
    bob.right(120)
    bob.forward(50)
    bob.right(120)
    bob.forward(40)
    bob.end_fill()
    bob.up()
    bob.goto(100,110)
    bob.down()

elif (l>=1 and c>=1 and n<1 and s<1 and len(password)>8):
    print("password is okay")

    #for orange
    bob.forward(150)
    bob.fillcolor("black")
    bob.begin_fill()
    bob.right(60)
    bob.forward(50)
    bob.right(120)
    bob.forward(50)
    bob.right(120)
    bob.forward(40)
    bob.end_fill()
    bob.up()
    bob.goto(100,110)
    characters = capital + lower + special+ special
    password = ''.join(random.choice(characters) for i in range(12))
    print("Suggested password to use:", password)

elif (l>=1 and c<1 and n<1 and s<1 or len(password)<6):
    print("password is bad")
    #for red
    bob.forward(225)
    bob.fillcolor("black")
    bob.begin_fill()
    bob.right(60)
    bob.forward(50)
    bob.right(120)
    bob.forward(50)
    bob.right(120)
    bob.forward(40)
    bob.end_fill()
    bob.up()
    bob.goto(100,110)
    bob.down()
    characters = capital + lower + special+ special
    password = ''.join(random.choice(characters) for i in range(12))
    print("Suggested password to use:", password)
   



###Refernece used: https://www.geeksforgeeks.org/python-program-check-validity-password/
###Refernece used: https://pynative.com/python-generate-random-string/ 







