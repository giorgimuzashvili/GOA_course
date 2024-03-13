from turtle import *

speed(7)

#we want to paint house

#step 1: draw a square

width(7)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square




#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()






penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
begin_fill
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw a window


penup()
goto(185, 185)
forward(10)
pendown()
color("red")
begin_fill()
left(30)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
right(90)
penup()
forward(130)
pendown()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

        



        





exitonclick()




