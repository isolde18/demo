import turtle #1-always start with import turtle
wn= turtle.Screen() #2-set up the window screen and its attributes
wn.bgcolor("purple") #such as background color
wn.title("Tri")#and name

tri=turtle.Turtle() #3-create tri and set some attributes 
tri.color("lightblue")#color
tri.pensize(5)#pen size

for i in range(3): #make tri draw equilateral triangle using the loop
    tri.forward(50)
    tri.left(120)
    tri.forward(50)

wn.mainloop()#wait for user to close window
