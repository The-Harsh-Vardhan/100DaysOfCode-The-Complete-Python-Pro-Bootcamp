from turtle import Turtle, Screen
#We have imported the Turtle Module
my_turtle = Turtle()
#We have taken the "Turtle" class and made an object "my_turtle"
#The class "Turtle" is from the module turtle

print(my_turtle)
#This is very different from string or integer, here an object is being printed

#car.speed from car get the speed module

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
#height and width of the screen on which our turtle appears
my_turtle.shape("turtle") #now the arrow turns into an actual turtle
my_turtle.color("coral")
#A function tied to an object is called a "method"


#Now the screen only closes on a click

#Move the Turtle Forward by 100 Units
print(my_turtle.position())
my_turtle.forward(100)
print(my_turtle.position())

my_screen.exitonclick()