import turtle
def draw_square(some_turtle):
   for i in range(1,5):
         some_turtle.forward(100)
         some_turtle.right(90)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    #create brad tutle
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("red")
    for i in range (1,36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()
draw_art()



