import turtle
import random


class Ball:
    def __init__(self, color=(0,0,0), size=100, vx=0, vy=0, px=0, py=0):
        self.color = color
        self.size = size
        self.speed_x = vx
        self.speed_y = vy
        self.position_x = px
        self.position_y = py

    def draw_circle(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.position_x,self.position_y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

def move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
    # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
    xpos[i] += vx[i]
    ypos[i] += vy[i]

    # if the ball hits the side walls, reverse the vx velocity
    if abs(xpos[i] + vx[i]) > (canvas_width - ball_radius):
        vx[i] = -vx[i]

    # if the ball hits the ceiling or the floor, reverse the vy velocity
    if abs(ypos[i] + vy[i]) > (canvas_height - ball_radius):
        vy[i] = -vy[i]

def initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
    # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
    for i in range(num_balls):
        xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
        ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
        vx.append(random.randint(1, 0.01*canvas_width))
        vy.append(random.randint(1, 0.01*canvas_height))
        ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

x = Ball()
x.draw_circle()