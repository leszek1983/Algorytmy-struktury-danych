import turtle

szachownica = turtle.Turtle()


szachownica.speed(8)
for i in range(4):
    szachownica.forward(800)
    szachownica.right(90)
a = 0
b = 0
for i in range(6):
    if(b == 0):
        a=1
    else:
        a=0
    for j in range(6):
        szachownica.penup()
        szachownica.goto(j*100, i*100*(-1))
        szachownica.pendown()
        if(a==0):
            szachownica.fillcolor('black')
            a=1
        else:
            szachownica.fillcolor('white')
            a=0
        szachownica.begin_fill()
        for k in range(4):
            szachownica.forward(100)
            szachownica.right(90)
        szachownica.end_fill()
    if(b==0):
        b=1
    else:
        b=0

# 1. Brak podawania parametrów z klawiatury
# 2. Proponuję zmienić nazewnictwo na bardziej czytelne
