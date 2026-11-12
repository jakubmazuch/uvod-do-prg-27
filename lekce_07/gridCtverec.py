import turtle


def ctverec(strana):
    for _ in range(4):
        zelva.forward(strana)
        zelva.left(90)


def mrizka(strana, pocetSloupcu, pocetRadku):
    for radek in range(pocetRadku):
        for sloupec in range(pocetSloupcu):
            zelva.penup()
            zelva.goto(strana*sloupec, strana*radek)
            zelva.pendown()
            ctverec(strana)


strana = int(input("Délka strany: "))
pocetSloupcu = int(input("Počet sloupců: "))
pocetRadku = int(input("Počet řádků: "))

zelva = turtle.Turtle()
zelva.shape("turtle")
zelva.speed(0)

mrizka(strana, pocetSloupcu, pocetRadku)

turtle.done()
