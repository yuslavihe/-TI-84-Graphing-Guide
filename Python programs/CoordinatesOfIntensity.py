import cv2
import csv

img = cv2.imread('text.png', cv2.IMREAD_GRAYSCALE)
threshold_lower_bound = 150

# detecting coordinates
height, width = img.shape
threshold_coordinates = []
for y in range(height):
    for x in range(width):
        if img[y, x] > threshold_lower_bound:
            threshold_coordinates.append((x, 165 - y))

# write to csv
with open('threshold_coordinates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(threshold_coordinates)
