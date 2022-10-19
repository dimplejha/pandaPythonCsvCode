
import csv
from csv import writer
from csv import reader

# with open("input.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         print(row)
#         x = row.split()
#         print(x)


# with open('input.csv', 'r') as read_obj, \
#         open('empty.csv', 'w', newline='') as write_obj:
#     # Create a csv.reader object from the input file object
#     csv_reader = reader(read_obj)
#     # Create a csv.writer object from the output file object
#     csv_writer = writer(write_obj)
#     # Read each row of the input csv file as list
#     for line in csv_reader:
#         print(line)
#         Type = line.split(",")
#         x = Type[1]
#         y = Type[2]
#         location = x, y
#         print(location)

#         # Append the default text in the row / list
#         line.append(location)
#         # Add the updated row / list to the output file
#         csv_writer.writerow(line)


readfile = open("input.csv", "r")

for line in readfile:
    Type = line.split(",")
    x = Type[1]
    y = Type[2]
    location = x, y
    print(location)
    line.append(location)
#         # Add the updated row / list to the output file
#         csv_writer.writerow(line)
# csv_reader.to_csv('file23456.csv')
