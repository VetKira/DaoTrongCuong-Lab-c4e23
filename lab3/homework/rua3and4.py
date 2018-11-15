from turtle import *

def draw_squared(length,colors) :
    color(colors)

    for i in range (4): 
        forward(length)
        left(90)

    # mainloop()

# draw_squared(90,"blue")


for i in range(30):
    draw_squared(i * 5, 'red')
    left(17)
    penup() #put pen up doesn't draw
    forward(i * 2)
    pendown() # put pen down draw
mainloop()
