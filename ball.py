import turtle
import random


class Ball:
    def __init__(self, color, size, vx, vy, px, py, width, height):
        self.color = color
        self.size = size
        self.speed_x = vx
        self.speed_y = vy
        self.position_x = px
        self.position_y = py
        self.width = width
        self.height = height

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_speed_x(self):
        return self.speed_x

    def get_speed_y(self):
        return self.speed_y

    def get_position_x(self):
        return self.position_x

    def get_position_y(self):
        return self.position_y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

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

    def move_circle(self, index):
        # update the x, y coordinates of ball i with velocity in the x (vx)
        # and y (vy) components
        self.position_x[index] += self.position_x[index]
        self.position_y[index] += self.position_y[index]

        # if the ball hits the side walls, reverse the vx velocity
        if (abs(self.position_x[index] + self.position_x[index])
                > (self.width - self.size)):
            self.position_x[index] = -self.position_x[index]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if (abs(self.position_y[index] + self.position_y[index])
                > (self.height - self.size)):
            self.position_y[index] = -self.position_y[index]

def initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
    # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
    for i in range(num_balls):
        xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
        ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
        vx.append(random.randint(1, 0.01*canvas_width))
        vy.append(random.randint(1, 0.01*canvas_height))
        ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
