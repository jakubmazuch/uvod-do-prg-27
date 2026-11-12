
import turtle

zelva = turtle.Turtle()
zelva.shape("turtle")
zelva.speed(3)

delka = 10

for _ in range(30):
    zelva.forward(delka)
    zelva.left(90)

    delka = delka + 5


turtle.done()
