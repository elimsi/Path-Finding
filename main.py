import cv2
import numpy as np
from Graph import Graph
import matplotlib.pyplot as plt

from animate import animate_search
import time

img = cv2.imread("map_source.png")

def image_to_grid(img):
    is_road = (img[:, :, 0] > 100) & (img[:, :, 1] > 100) & (img[:, :, 2] > 100)
    grid = np.zeros(img.shape[:2], dtype=np.uint8)
    grid[is_road] = 255
    return grid

grid = image_to_grid(img)
graph = Graph(grid)

import time
import random as r
from math import *

def distance_2points(case1,case2):
    return(np.round(sqrt((case2[0]-case1[0])**2 + (case2[1]-case1[1])**2),3))

def inter_cercle(M,centre,rayon,couleur):
    cx,cy=centre
    tab_case=[[(i,j) for i in range(round(cx-rayon),round(cx+rayon)+1)] for j in range(round(cy-rayon),round(cy+rayon)+1)]
    for l_case in tab_case:
        for case in l_case:
            if distance_2points(case,centre)<=rayon and np.mean(M[case])>=100:
                M[case]=couleur

c1=np.array([0,0,200])
c4=np.array([0,255,255])

inter_cercle(img,(345,465),40,c1)
inter_cercle(img,(225,254),40,c1)

for _ in range(15):
    a,b=r.randint(100,700),r.randint(400,1000)
    inter_cercle(img,(a,b),35,c4)

depart=(434,615)
arrivee=(1018,50)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

print("Running BFS...")
t0 = time.time()
path, order = graph.BFS(depart, arrivee)
t1 = time.time()
print(f"BFS finished in {t1 - t0:.3f} seconds.")
if path:
    plt.plot([x for x, _ in path], [y for _, y in path], "r-", label="BFS")

print("Running A*...")
t0 = time.time()
path1, order1 = graph.A_star(depart, arrivee)
t1 = time.time()
print(f"A* finished in {t1 - t0:.3f} seconds.")
if path1:
    plt.plot([x for x, _ in path1], [y for _, y in path1], "c--", label="A*")
    print("Generating A* animation...")
    animate_search("map_source.png", order1, path1, "astar_exploration.gif", n_frames=40)

print("Running Dijkstra...")
t0 = time.time()
path2, order2 = graph.djikstra(depart, arrivee)
t1 = time.time()
print(f"Dijkstra finished in {t1 - t0:.3f} seconds.")
if path2:
    plt.plot([x for x, _ in path2], [y for _, y in path2], "g-", label="Dijkstra")
    print("Generating Dijkstra animation...")
    animate_search("map_source.png", order2, path2, "dijkstra_exploration.gif", n_frames=40)

plt.legend()
plt.savefig("result_comparison.png")
# plt.show()
