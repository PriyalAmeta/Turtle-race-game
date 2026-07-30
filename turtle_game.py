import turtle
import random

canvas = turtle.Screen()
canvas.title("Turtle Race")
canvas.setup(width=700, height=700)
canvas.update()
canvas.bgcolor("misty rose")

number= int(input("Enter the number of turtules you want: "))
n=1
racer_list=[]
while(n<=number):
        racer=turtle.Turtle()
        racer_list.append(racer)
        n+=1

finishing_turtle = turtle.Turtle()

writer = turtle.Turtle()#displays result
writer.hideturtle()
writer.penup()

#appearance
i=1
for racer in racer_list:
       paint=input(f"enter color of turtle {i}: ")
       racer.color(paint)
       racer.shape("turtle")
       i+=1

finishing_turtle.color("black")

#positions
width=600
if number==1:
        start=0
        spacing=0
else:
        spacing = width / (number-1)
        start=-width/2
for racer in racer_list:
       racer.penup()
       racer.left(90)
       racer.goto(start,-260)
       start=start+spacing

finishing_turtle.penup()
finishing_turtle.goto(-300,260)
finishing_turtle.pensize(2)
finishing_turtle.pendown()
finishing_turtle.forward(600)
finishing_turtle.hideturtle()

#motion
race = True
while race:
        for racer in racer_list:
                racer.forward(random.randrange(10,50))
                if racer.ycor()>=finishing_turtle.ycor():
                        writer.goto(0,0)
                        writer.write(
                        f"{racer.pencolor()} wins!",
                        align="center",
                        font=("Comic Sans MS", 22, "bold")
                        )

                        race=False
                        break

canvas.exitonclick()