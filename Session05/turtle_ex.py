from turtle import *
#.1
def prx3():
    for i in range(3):
        print('Hello')

#.2
def calc(x,y):
    tong = x + y
    print(tong)
calc(3,7)

#.3
def draw_square(lenght,Color):
    for i in range(4):
        color(Color)
        forward(lenght)
        left(90)
draw_square(100,'red')
mainloop()

#.4
def draw_square(length,color):
    length = i * 5
    color = 'red'

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

#.5
def draw_star(x,y,lenght):
    forward(lenght)
    left(x)
    right(y)
for i in range(5):
    x = 0
    y = 144
    lenght = 100
    draw_star(x,y,lenght)

#.6
def draw_star(x,y,lenght):
    forward(lenght)
    left(x)
    right(y)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)


   