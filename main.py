import cv2
import numpy as np
from Graph import Graph
import matplotlib.pyplot as plt

img = cv2.imread("lol.png")

def image_to_grid(img):
    is_road = (img[:, :, 0] > 100) & (img[:, :, 1] > 100) & (img[:, :, 2] > 100)
    grid = np.zeros(img.shape[:2], dtype=np.uint8)
    grid[is_road] = 255
    return grid

grid = image_to_grid(img)
graph = Graph(grid)
