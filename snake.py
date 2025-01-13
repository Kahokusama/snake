# snake.py

from settings import BLOCK_SIZE, GREEN

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # 蛇身初始位置
        self.direction = (BLOCK_SIZE, 0)  # 初始向右移動
        self.alive = True
    
    def move(self):
        # 計算蛇頭的新位置
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        # 在蛇尾添加一個區塊
        tail_x, tail_y = self.body[-1]
        dir_x, dir_y = self.direction
        new_tail = (tail_x - dir_x, tail_y - dir_y)  # 在蛇尾添加一個新區塊
        self.body.append(new_tail)

    def check_collision(self):
        # 檢查蛇是否撞牆或撞到自己
        head = self.body[0]
        # 撞牆
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            self.alive = False
        # 撞到自己
        if head in self.body[1:]:
            self.alive = False
    
    def draw(self, painter):
        for segment in self.body:
            painter.setBrush(GREEN)
            painter.drawRect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE)
