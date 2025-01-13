# main.py

import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter
from snake import Snake
from food import Food
from settings import WIDTH, HEIGHT, BLOCK_SIZE, FPS, BLACK

class SnakeGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("貪食蛇遊戲")
        self.setGeometry(100, 100, WIDTH, HEIGHT)
        self.setStyleSheet("background-color: black;")
        
        self.snake = Snake()
        self.food = Food()
        
        # 定時器更新遊戲
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(1000 // FPS)
        
        self.setFocusPolicy(Qt.StrongFocus)
        
    def update_game(self):
        if not self.snake.alive:
            self.timer.stop()
            return
        
        self.snake.move()
        
        # 檢查是否吃到食物
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.randomize_position()

        # 檢查碰撞
        self.snake.check_collision()
        
        self.update()  # 重繪畫面
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left and self.snake.direction != (BLOCK_SIZE, 0):
            self.snake.direction = (-BLOCK_SIZE, 0)
        elif event.key() == Qt.Key_Right and self.snake.direction != (-BLOCK_SIZE, 0):
            self.snake.direction = (BLOCK_SIZE, 0)
        elif event.key() == Qt.Key_Up and self.snake.direction != (0, BLOCK_SIZE):
            self.snake.direction = (0, -BLOCK_SIZE)
        elif event.key() == Qt.Key_Down and self.snake.direction != (0, -BLOCK_SIZE):
            self.snake.direction = (0, BLOCK_SIZE)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 繪製蛇和食物
        self.snake.draw(painter)
        self.food.draw(painter)
        
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = SnakeGame()
    game.show()
    sys.exit(app.exec_())
