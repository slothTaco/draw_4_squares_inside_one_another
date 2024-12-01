#Draw 4 squares inside each other

from turtle import*

#square
for sides in range (4):
    forward(50)
    left(90)

#new location
penup()
right(90)
forward(25)
right(90)
forward(25)
right(180)
pendown()

#square
for sides in range (4):
    forward(100)
    left(90)

#new location
penup()
right(90)
forward(50)
right(90)
forward(50)
right(180)
pendown()

#square
for sides in range (4):
    forward(200)
    left(90)

#new location
penup()
right(90)
forward(100)
right(90)
forward(100)
right(180)
pendown()

#square
for sides in range (4):
    forward(400)
    left(90)
