import numpy as np
import warnings
warnings.filterwarnings('ignore')


class Grid:
    def __init__(self):
        self.grid = np.zeros((10, 10)).astype(int)
    def visualize(self):
        print(self.grid)
    def place_items(self, obstacles, player, goal):
        for obstacle in obstacles:
            self.grid[obstacle[0], obstacle[1]] = -1
        self.grid[player.x, player.y] = 1
        self.grid[goal[0], goal[1]] = 96 
    def calc_penalty(self, movement, grid):
        penalty = 0
        x, y = movement
        if x > 0 and y > 0 and self.grid[x - 1, y - 1] == -1: penalty += 1
        if x < 9 and y < 9 and self.grid[x + 1, y + 1] == -1: penalty += 1
        if x > 0 and y < 9 and self.grid[x - 1, y + 1] == -1: penalty += 1
        if x < 9 and y > 0 and self.grid[x + 1, y - 1] == -1: penalty += 1
        if x < 9 and self.grid[x + 1, y] == -1: penalty += 1
        if x > 0 and self.grid[x - 1, y] == -1: penalty += 1
        if y < 9 and self.grid[x, y + 1] == -1: penalty += 1
        if y > 0 and self.grid[x, y - 1] == -1: penalty += 1
        return penalty
    def update(self, player):
        cur_pos = player
        directions = ['up', 'left', 'right', 'down', 'up_left', 'up_right', 'down_right', 'down_left']
        best_dist = 100
        best_penalty = 10
        best_direction = ''
        for direction in directions:
            movement = player.move(direction)
            dist = distance(movement, [9, 9])
            if dist < best_dist and self.grid[movement[0], movement[1]] != -1 and dist > 0:
                best_dist = dist
                best_direction = direction
        player.move(best_direction, act = True)
        self.grid[cur_pos.x, cur_pos.y] = 0
        self.grid[player.x, player.y] = 1
    def add_obstacles(self, n_obstacles):
        for i in range(n_obstacles):
            obstacle = [np.random.randint(0, 9), np.random.randint(0, 9)]
            if self.grid[obstacle[0], obstacle[1]] == 0:
                self.grid[obstacle[0], obstacle[1]] = -1

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, direction, act = False):
        x, y = self.x, self.y
        if direction == 'up':
            if x > 0: x -= 1
            if act: self.x, self.y = x, y
            else: return [x, y]
        elif direction == 'down':
            if x < 9: x += 1
            if act: self.x, self.y = x, y
            else: return [x, y]
        elif direction == 'left':
            if y > 0: y -= 1
            if act: self.x, self.y = x, y
            else: return [x, y]
        elif direction == 'right':
            if y < 9: y += 1
            if act: self.x, self.y = x, y
            else: return [x, y]
        elif direction == 'up_left':
            if x > 0 and y > 0: x, y = x - 1, y - 1
            if act: self.x, self.y = x, y
            else: return [x, y]
        elif direction == 'down_left':
            if x < 9 and y > 0: x, y = x + 1, y - 1
            if act: self.x, self.y = x, y
            else: return [x, y]
        elif direction == 'up_right':
            if x > 0 and y < 9: x, y = x - 1, y + 1
            if act: self.x, self.y = x, y
            else: return [x, y]
        elif direction == 'down_right':
            if x < 9 and y < 9: x, y = x + 1, y + 1
            if act: self.x, self.y = x, y
            else: return [x, y]

def distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

grid = Grid()
player = Player()

grid.place_items(obstacles = [[9, 7], [8, 7], [6, 7], [6, 8]], player = player, goal = [9, 9])

grid.add_obstacles(20)

for i in range(100):
    grid.update(player)

grid.visualize()



