import turtle

# ekranas
screen = turtle.Screen()
screen.title("Kalėdų sveikinimas")
screen.bgcolor("white")

# vezlio ypatybes
t = turtle.Turtle()
t.speed(3)
t.width(2)


# Funkcija piesti eglute
def draw_triangle(color, length):
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()


# egles sluoksniu funkcija
def draw_christmas_tree():
    # 1 sluoksnis
    t.penup()
    t.goto(-75, -125)
    t.pendown()
    draw_triangle("blue", 150)

    # 2 sluoksnis
    t.penup()
    t.goto(-60, -62)
    t.pendown()
    draw_triangle("blue", 120)

    # 3 sluoksnis
    t.penup()
    t.goto(-45, 0)
    t.pendown()
    draw_triangle("blue", 90)

    #kamienas
    t.penup()
    t.goto(-15, -100)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(30)
        t.right(90)
        t.forward(40)
        t.right(90)
    t.end_fill()

#apskritimai egles viduje
def draw_circles():
    t.penup()
    t.color("green")
    t.goto(0,0)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.color("green")
    t.goto(28, -33)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.color("green")
    t.goto(-18, 34)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.color("green")
    t.goto(15, 34)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.color("green")
    t.goto(-20, -45)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.color("green")
    t.goto(20, -75)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.color("green")
    t.goto(30, -110)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.color("green")
    t.goto(-30, -125)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.color("green")
    t.goto(-25, -85)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

# sveikinimo funkcija
def write_greeting1():
    t.penup()
    t.goto(-35, 100)
    t.pendown()
    t.color("grey")
    t.write("Šventų", font=("Arial", 18, "bold"))

def write_greeting2():
    t.penup()
    t.goto(-50, -200)
    t.pendown()
    t.color("grey")
    t.write("Kalėdų!", font=("Arial", 18, "bold"))


# Piešiame eglutę
draw_christmas_tree()

#sveikinimas
write_greeting1()
write_greeting2()

#apskritimu piesimas
draw_circles()

# stop kad neuzsidarytu
t.hideturtle()
turtle.done()