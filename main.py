from turtle import Screen
import time
from snake import snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
scoreboard = Scoreboard()

food = Food()
serp = snake()
screen.listen()
screen.onkey(serp.up, "Up")
screen.onkey(serp.right, "Right")
screen.onkey(serp.left, "Left")
screen.onkey(serp.down, "Down")
while True:
    screen.update()
    time.sleep(0.1)
    serp.mover()

    if serp.cabeza.distance(food) < 15:
        serp.extender()
        food.refresh()
        scoreboard.increaseScore()
    if (
        serp.cabeza.xcor() > 290
        or serp.cabeza.xcor() < -290
        or serp.cabeza.ycor() > 295
        or serp.cabeza.ycor() < -300
    ):
        scoreboard.reset()
        break
    for cuadrado in serp.cuadrados[1:]:
        if serp.cabeza.distance(cuadrado) < 10:
            scoreboard.reset()
            break

screen.exitonclick()


# cuadrados = []
# posicion = [(0, 0), (-20, 0), (-40, 0)]
# for coordenada in posicion:
#     cuadrado = Turtle(shape="square")
#     cuadrado.color("white")
#     cuadrado.penup()
#     cuadrado.goto(coordenada)
#     cuadrados.append(cuadrado)


# for cuad in range(len(cuadrados) - 1, 0, -1):
#     nuevaX = cuadrados[cuad - 1].xcor()
#     nuevaY = cuadrados[cuad - 1].ycor()
#     cuadrados[cuad].goto(x=nuevaX, y=nuevaY)
# cuadrados[0].forward(20)
# cuadrados[0].left(90)
