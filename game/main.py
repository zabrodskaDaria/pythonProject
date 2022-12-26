from tkinter import *
import time
import random

tk = Tk()
tk.title('Game')

tk.resizable(0, 0)

tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=500, height=400, highlightthickness=0)

canvas.pack()

tk.update()

""" Описываем класс Ball, который будет отвечать за шарик"""

class Ball:

    def __init__(self, canvas, paddle, score, color):

        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        """ Цвет нужен был для того, чтобы мы им закрасили весь шарик
         здесь появляется новое свойство id, в котором хранится внутреннее название шарика
         а ещё командой create_oval мы создаём круг радиусом 15 пикселей и закрашиваем нужным цветом """

        self.id = canvas.create_oval(10,10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-2, -1, 1, 2]

        random.shuffle(starts)

        """ Вектор движения шарика"""

        self.x = starts[0]
        self.y = -2

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False


    """ Обрабатываем касание платформы, для этого получаем 4 координаты шарика в переменной pos 
         (левая верхняя и правая нижняя точки)"""

    def hit_paddle(self, pos):

        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:

                self.score.hit()

                return True

        return False

    """  Движение шарика"""

    def draw(self):

        self.canvas.move(self.id, self.x, self.y)

        """Новые координаты шарика"""

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:

            self.y = 2

        if pos[3] >= self.canvas_height:

            self.hit_bottom = True

            canvas.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='red')

        if self.hit_paddle(pos) == True:

            self.y = -2

        if pos[0] <= 0:

            self.x = 2

        if pos[2] >= self.canvas_width:

            self.x = -2

    """Описываем класс Paddle, который отвечает за платформы"""
class Paddle:

    def __init__(self, canvas, color):

        self.canvas = canvas

        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)

        start_1 = [40, 60, 90, 120, 150, 180, 200]

        random.shuffle(start_1)

        self.starting_point_x = start_1[0]

        self.canvas.move(self.id, self.starting_point_x, 300)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        """ Задаём обработчик нажатий"""

        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)

        self.started = False

        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    def turn_right(self, event):

        self.x = 2

    def turn_left(self, event):

        self.x = -2

        """Игра начинается"""
    def start_game(self, event):

        """ Меняем значение переменной, которая отвечает за старт движения платформы"""

        self.started = True

    def draw(self):

        self.canvas.move(self.id, self.x, 0)

        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:

            self.x = 0

        elif pos[2] >= self.canvas_width:

            self.x = 0

"""  Описываем класс Score, который отвечает за отображение счетов"""

class Score:

    def __init__(self, canvas, color):

        self.score = 0

        self.canvas = canvas

        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    """ Обрабатываем касание платформы"""

    def hit(self):

        self.score += 1

        self.canvas.itemconfig(self.id, text=self.score)

""" Создание объектов"""

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'White')
ball = Ball(canvas, paddle, score, 'red')

while not ball.hit_bottom:

    if paddle.started == True:
        ball.draw()
        paddle.draw()


    """ Обновляем  игровое поле"""

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

time.sleep(3)



