from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class snake:
    def __init__(self):
        self.cuadrados = []
        self.posicion = [(0, 0), (-20, 0), (-40, 0)]
        self.crear_cuerpo()
        self.cabeza = self.cuadrados[0]

    def crear_cuerpo(self):
        for coordenada in self.posicion:
            self.añadir_cuerpo(coordenada)

    def añadir_cuerpo(self, posicion):
        cuadrado = Turtle(shape="square")
        cuadrado.color("white")
        cuadrado.penup()
        cuadrado.goto(posicion)
        self.cuadrados.append(cuadrado)

    def extender(self):
        self.añadir_cuerpo(self.cuadrados[-1].position())

    def mover(self):
        for cuad in range(len(self.cuadrados) - 1, 0, -1):
            nuevaX = self.cuadrados[cuad - 1].xcor()
            nuevaY = self.cuadrados[cuad - 1].ycor()
            self.cuadrados[cuad].goto(x=nuevaX, y=nuevaY)
        self.cabeza.forward(20)

    def up(self):
        if self.cabeza.ycor() != self.cuadrados[1].ycor() - 20:
            self.cabeza.setheading(UP)

    def right(self):
        if self.cabeza.xcor() != self.cuadrados[1].xcor() - 20:
            self.cabeza.setheading(RIGHT)

    def left(self):
        if self.cabeza.xcor() != self.cuadrados[1].xcor() + 20:
            self.cabeza.setheading(LEFT)

    def down(self):
        if self.cabeza.ycor() != self.cuadrados[1].ycor() + 20:
            self.cabeza.setheading(DOWN)
