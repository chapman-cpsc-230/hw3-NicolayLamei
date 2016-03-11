num_sides = int (input ("Enter Number of Sides:"))
side_len = int (input ("Enter the Length of Each Side:"))

import turtle
t = turtle.Pen()


def draw_reg_polygon (t,num_sides,side_len):
    for i in range (num_sides):
        t.forward(side_len)
        t.left(360/num_sides)

bob = turtle.Pen()

#side = 10
for j in range (1):
    draw_reg_polygon(bob,num_sides,side_len)
    #draw_square(bob,side)
    #side += 5

stopper = input("Hit <enter> to quit.")

turtle.bye()
