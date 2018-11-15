from turtle import *


def draw_star(x,y,length):
    penup()
    setposition(x,y)
    #https://stackoverflow.com/questions/48106441/how-do-i-teleport-the-turtle-in-python
    pendown()
    for i in range(5):
        forward(length)
        right(144)
    # mainloop()

# draw_star(0,0,180)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300) #ve~ sao random 1 vi tri tren man hinh
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)


mainloop()



