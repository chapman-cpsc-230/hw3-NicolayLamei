num_sides = int(input("Enter the an odd number of sides (at least 5): "))
side_len = int(input("Enter the length of each side:"))

import turtle
t = turtle.Pen()

### MAM: This draws a regular polygon, not a star.
def draw_star(t,num_sides,side_len):
    for i in range (num_sides):
        t.forward(side_len)
        t.left(360/num_sides)

bob = turtle.Pen()
bob.penup()
bob.goto(-side_len/2,0)
bob.pendown()

for j in range (num_sides):
    draw_star(bob,1,side_len)  ##$ MAM: Draw a one-sides regular polygon? Weird.
    bob.left(180-(180/num_sides))


### MAM: You are using puython 3. This makes it complicated for me to debug,
### because this line will crash for me. (I have to replace 'input' with 'raw_input'
stopper = input("Hit <enter> to quit.")

turtle.bye()
