import csv

input_file = "temp.txt"
output_file = "coordinates.csv"

# read data from the input file
def read_input_data(file):
    x1, x2, y = [], [], []
    with open(file, 'r') as f:
        for line in f:
            x1_temp, x2_temp, y_temp = map(int, line.strip().split())
            x1.append(x1_temp)
            x2.append(x2_temp)
            y.append(y_temp)
    return x1, x2, y

# generate final coordinates
def final_coordinates(x1, x2, y):
    x_final, y_final = [], []
    for xi1, xi2, yi in zip(x1, x2, y):
        x_final.extend([xi1, xi2])
        y_final.extend([yi, yi])
    return x_final, y_final

#  write coordinates to a CSV file
def write_coordinates(file, x_final, y_final):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for x_val, y_val in zip(x_final, y_final):
            writer.writerow([x_val, y_val])

# Main code
x1, x2, y = read_input_data(input_file)
x_final, y_final = final_coordinates(x1, x2, y)
write_coordinates(output_file, x_final, y_final)
