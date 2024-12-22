import re
import numpy as np

with open('data.txt') as f:
    lines = f.readlines()

positions = []
velocities = []
pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"
for i in range(len(lines)):
    matches = re.search(pattern, lines[i])
    x = int(matches.group(1))
    y = int(matches.group(2))
    positions.append((x, y))
    vx = int(matches.group(3))
    vy = int(matches.group(4))
    velocities.append((vx, vy))

WIDTH = 101
HEIGHT = 103

map = np.zeros((HEIGHT, WIDTH), dtype=int)

for i in range(len(lines)):
    x, y = positions[i]
    vx, vy = velocities[i]
    for t in range(100):
        x = (x + vx) % WIDTH
        y = (y + vy) % HEIGHT
    map[y][x] += 1

Q1, Q2, Q3, Q4 = [], [], [], []
for i in range(len(map)):
    if i < HEIGHT//2:
        Q1.append(map[i][:WIDTH//2])
        Q2.append(map[i][WIDTH//2+1:])
    if i > HEIGHT//2:
        Q3.append(map[i][:WIDTH // 2])
        Q4.append(map[i][WIDTH // 2 + 1:])
print(np.sum(Q1)*np.sum(Q2)*np.sum(Q3)*np.sum(Q4))


map2 = np.zeros((HEIGHT, WIDTH), dtype=int)

X = 1247


np.set_printoptions(threshold=np.inf, linewidth=np.inf)
for t in range(100):
    map2 = np.zeros((HEIGHT, WIDTH), dtype=int)
    for i in range(len(lines)):
        x, y = positions[i]
        vx, vy = velocities[i]
        x = (x + vx) % WIDTH
        y = (y + vy) % HEIGHT
        positions[i] = (x, y)
        map2[y][x] += 1
    if t > 50:
        print("Time elapsed (s): ", t+1)
        print(np.where(map2 == 0, '.', map2))
