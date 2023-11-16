import turtle
import ball

class Interface:
    def __init__(self):
        self.num_balls = int(input("Number of balls to simulate: "))
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.__canvas_width = turtle.screensize()[0]
        self.__canvas_height = turtle.screensize()[1]
        self.__ball_radius = 0.05 * self.__canvas_width
        turtle.colormode(255)
        self.color_list = []
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
    def generate(self):
        pass

    def run(self):
        while (True):
            turtle.clear()
            for i in range(self.num_balls):
                ball.draw_circle(ball_color[i], ball_radius, xpos[i], ypos[i])
                ball.move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius)
            turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
