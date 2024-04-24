import csv

input_file = 'coordinates.csv'
output_file = 'shade.csv'
density = 2

# read coordinates from file
def read_coordinates(file):
    x_coords, y_coords = [], []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for x, y in reader:
            x_coords.append(int(x))
            y_coords.append(int(y))
    return x_coords, y_coords

# interpolate coordinates based on colour density
def interpolate_coordinates(x_coords, y_coords, density):
    interpolated_x, interpolated_y = [], []
    for i in range(len(x_coords) - 1):
        x1, y1 = x_coords[i], y_coords[i]
        x2, y2 = x_coords[i + 1], y_coords[i + 1]
        delta_x = x2 - x1
        delta_y = y2 - y1
        distance = max(abs(delta_x), abs(delta_y))
        if distance > 0:
            step_x = delta_x / distance
            step_y = delta_y / distance
            for j in range(int(distance)):
                interpolated_x.append(int(x1 + j * step_x))
                interpolated_y.append(int(y1 + j * step_y))
    return interpolated_x, interpolated_y

# write coordinates to a CSV file
def write_coordinates(file, x_coords, y_coords):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for x, y in zip(x_coords, y_coords):
            writer.writerow([x, y])

# Main code
x_coords, y_coords = read_coordinates(input_file)
x_final, y_final = interpolate_coordinates(x_coords, y_coords, density)
write_coordinates(output_file, x_final, y_final)
