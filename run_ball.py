import turtle
import ball
import random
class Interface:
    def __init__(self):
        self.__num_balls = int(input("Number of balls to simulate: "))
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.__canvas_width = turtle.screensize()[0]
        self.__canvas_height = turtle.screensize()[1]
        self.__ball_radius = 0.05 * self.__canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

    def generate(self):
        # create random number of balls, num_balls, located at random
        # positions within the canvas; each ball has a random velocity
        # value in the x and y direction and is painted with a random color
        for i in range(self.__num_balls):
            self.xpos.append(random.randint(-1 * self.__canvas_width
                                            + self.__ball_radius,
                                            self.__canvas_width
                                            -self.__ball_radius))
            self.ypos.append(random.randint(-1 * self.__canvas_height
                                            + self.__ball_radius,
                                            self.__canvas_height
                                            - self.__ball_radius))
            self.vx.append(random.randint(1, 0.01 * self.__canvas_width))
            self.vy.append(random.randint(1, 0.01 * self.__canvas_height))
            self.ball_color.append((random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255)))

    def run(self):
        balls = ball.Ball(self.ball_color, self.__ball_radius, self.vx, self.vy,
                          self.xpos, self.ypos, self.__canvas_width,
                          self.__canvas_height)
        while True:
            turtle.clear()
            for i in range(self.__num_balls):
                balls.draw_circle(i)
                balls.move_circle(i)
            turtle.update()
        turtle.done()

# hold the window; close it by clicking the window close 'x' mark
if __name__ == '__main__':
    t = Interface()
    t.generate()
    t.run()