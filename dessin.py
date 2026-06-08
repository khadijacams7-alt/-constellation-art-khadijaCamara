import turtle
import random

# Fenêtre
screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("midnight blue")
screen.title("Constellation du Cheval Ailé")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Fond étoilé
for _ in range(150):
    t.penup()
    x = random.randint(-450, 450)
    y = random.randint(-350, 350)
    t.goto(x, y)
    t.dot(random.randint(2, 5), "white")

# Points de la constellation
points = [
    (-250, 80),   # nez
    (-220, 120),  # tête
    (-180, 140),  # crinière
    (-120, 90),   # cou
    (-50, 20),    # poitrine
    (50, 50),     # dos
    (130, 20),    # arrière
    (200, 40),    # queue

    (-40, -50),   # ventre
    (-80, -120),  # patte avant
    (-110, -180), # sabot avant

    (70, -70),    # patte arrière
    (110, -140),  # genou
    (150, -210),  # sabot

    (0, 120),     # aile 1
    (70, 200),    # aile 2
    (140, 260),   # aile 3
    (220, 180)    # pointe aile
]

# Dessin des étoiles principales
for x, y in points:
    t.penup()
    t.goto(x, y)
    t.dot(14, "white")

# Relier les étoiles
t.color("cyan")
t.pensize(3)

def relier(a, b):
    t.penup()
    t.goto(points[a])
    t.pendown()
    t.goto(points[b])

# Corps
relier(0,1)
relier(1,2)
relier(2,3)
relier(3,4)
relier(4,5)
relier(5,6)
relier(6,7)

# Ventre
relier(4,8)
relier(8,6)

# Patte avant
relier(8,9)
relier(9,10)

# Patte arrière
relier(8,11)
relier(11,12)
relier(12,13)

# Aile
relier(4,14)
relier(14,15)
relier(15,16)
relier(16,17)
relier(15,5)

turtle.done()