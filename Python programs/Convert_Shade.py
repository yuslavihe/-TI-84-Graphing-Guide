import csv

input_file = "temp-f"
output_file_shade = "shade.csv"
output_file_shade_deco = "shade_deco.csv"

# First part of the code
x1 = []
x2 = []
y = []
x_final = []
y_final = []

with open(input_file, 'r') as f:
    for line in f:
        x1_temp, x2_temp, y_temp = map(int, line.strip().split())
        x1.append(x1_temp)
        x2.append(x2_temp)
        y.append(y_temp)

index = 0
for yi in y:
    y_final.append(yi)
    y_final.append(yi)
    x_final.append(x1[index])
    x_final.append(x2[index])
    index += 1
with open(output_file_shade, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for x_val, y_val in zip(x_final, y_final):
        writer.writerow([x_val, y_val])

# Second part of the code
x_shade = []
y_shade = []
density_x = 2
density_y = 1

for _ in range(2):
    x_final.append(x_final[-2])
    y_final.append(y_final[-2]-1)

print(len(x_final), len(y_final))

index = 0
while 2 * index < len(y):
    x1, x2 = x_final[2*index], x_final[2*index+1]
    i = y[2*index]
    while x1 <= x2:
        x_shade.append(x1)
        x1 += density_x
        y_shade.append(i)
    index += density_y

with open(output_file_shade_deco, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for x_val, y_val in zip(x_shade, y_shade):
        writer.writerow([x_val, y_val])
