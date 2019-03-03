from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for c in colors:
    color(c)
    begin_fill()
    for i in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    end_fill()
    forward(100)



mainloop()