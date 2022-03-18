import turtle

win = turtle.Screen()
win.bgcolor("light green")
win.title("Belajar Turtle")
win.setup(width=600, height=600)

t = turtle.Turtle()
jumlah = int(input("banyak lingkaran:"))
jari2 = int(input("jari jari lingkaran:"))
jarak = int(input("jarak antara lingkaran:"))
for i in range(jumlah):
    t.circle(jari2)
    t.penup()
    t.forward(jarak)
    t.pendown()
