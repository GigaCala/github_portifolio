from tkinter import *
import time
import random

class Ball:
    def __init__(self, paddle, score, canvas, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score =  score
        self.id = canvas.create_oval(10, 10, 50, 50, fill=color)
        self.canvas.move(self.id, 245, 100)
        movement = [-3, -2, -1, 2, 3]
        random.shuffle(movement)
        self.x = movemen[0]
        self.y = -3
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        hit_efom = False

    def draw_ball(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            hit_efom =  True
            self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2, text="Game Over", fill="red", font=('Helvetica', 50))
        if self.hit_paddle(pos):
            self.y = -6
            self.score.increment()
        if pos[0] <= 0:
            self.y = -3
        if pos[2] >= self.canvas_width():
            self.y = -3

    def hit_paddle(self, pos):
        paddle_pos = self.paddle.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] <= paddle_pos[1] and pos[3] > 
            
