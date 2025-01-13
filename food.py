# food.py

import random
from settings import BLOCK_SIZE, RED

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()
    
    def randomize_position(self):
        # 隨機生成食物位置
        self.position = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                         random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)
    
    def draw(self, painter):
        painter.setBrush(RED)
        painter.drawRect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE)
